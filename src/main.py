from fastapi import FastAPI
import numpy as np
import sys
sys.path.append("src")
from drift_detector import DriftDetector

app = FastAPI()


@app.get("/")
def home():
    return {"message": "ML Canary is running!"}


@app.get("/check-drift")
def check_drift():

    reference_data = np.array([1.0, 2.0, 3.0, 4.0, 50])

    live_data = np.array([8.0, 9.0, 10.0, 11.0, 12.0, 8.5, 9.5, 10.5])

    detector = DriftDetector(reference_data, num_bins=5)
    psi_score = detector.calculate_psi(live_data)
    interpretation = detector.interpret_psi(psi_score)

    return {
        "psi_score": psi_score,
        "interpretation": interpretation

    }