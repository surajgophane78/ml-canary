from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import List
from prometheus_client import Gauge, generate_latest
import numpy as np
import sys
sys.path.append("src")
from drift_detector import DriftDetector
from alert import send_telegram_alert
from datetime import datetime, timedelta

app = FastAPI()

psi_gauge = Gauge("drift_psi_score", "Current PSI score for drift detection")
last_alert_time = None
COOLDOWN_MINUTES = 5


@app.get("/")
def home():
    return {"message": "ML Canary is running!"}


@app.get("/check-drift")
def check_drift():
    reference_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    live_data = np.array([8.0, 9.0, 10.0, 11.0, 12.0, 8.5, 9.5, 10.5])

    detector = DriftDetector(reference_data, num_bins=5)
    psi_score = detector.calculate_psi(live_data)
    interpretation = detector.interpret_psi(psi_score)

    return {"psi_score": psi_score, "interpretation": interpretation}


class LiveDataInput(BaseModel):
    live_values: List[float]


@app.post("/check-drift-custom")
def check_drift_custom(data: LiveDataInput):
    global last_alert_time

    reference_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    live_data = np.array(data.live_values)

    detector = DriftDetector(reference_data, num_bins=5)
    psi_score = detector.calculate_psi(live_data)
    interpretation = detector.interpret_psi(psi_score)

    psi_gauge.set(psi_score)

    if psi_score > 0.2:
        now = datetime.now()
        if last_alert_time is None or (now - last_alert_time) > timedelta(minutes=COOLDOWN_MINUTES):
            alert_message = f"🚨 ML Canary Alert!\nPSI Score: {psi_score:.4f}\nStatus: {interpretation}"
            send_telegram_alert(alert_message)
            last_alert_time = now

    return {"psi_score": psi_score, "interpretation": interpretation}