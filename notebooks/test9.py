import yfinance as yf
import numpy as np
import sys
sys.path.append("src")
from drift_detector import DriftDetector

stock = yf.Ticker("RELIANCE.NS")
data = stock.history(period="2mo")
close_prices = data["Close"].values

# Daily % return calculate karo (aaj ka price - kal ka price) / kal ka price
daily_returns = np.diff(close_prices) / close_prices[:-1] * 100

reference_data = daily_returns[:25]
live_data = daily_returns[25:]

print("Reference data points:", len(reference_data))
print("Live data points:", len(live_data))

detector = DriftDetector(reference_data, num_bins=5)
psi_score = detector.calculate_psi(live_data)
interpretation = detector.interpret_psi(psi_score)

print(f"\nPSI Score: {psi_score:.4f}")
print(f"Interpretation: {interpretation}")