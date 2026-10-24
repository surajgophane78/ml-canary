import yfinance as yf
import numpy as np
import sys
sys.path.append("src")
from drift_detector import DriftDetector
from alert import send_telegram_alert


def get_daily_returns(symbol, period="3mo"):
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    close_prices = data["Close"].values
    daily_returns = np.diff(close_prices) / close_prices[:-1] * 100
    return daily_returns


def check_stock_drift(symbol, reference_days=40, num_bins=4):
    returns = get_daily_returns(symbol, period="3mo")

    reference_data = returns[:reference_days]
    live_data = returns[reference_days:]

    detector = DriftDetector(reference_data, num_bins=num_bins)
    psi_score = detector.calculate_psi(live_data)
    interpretation = detector.interpret_psi(psi_score)

    print(f"Stock: {symbol}")
    print(f"Reference points: {len(reference_data)}, Live points: {len(live_data)}")
    print(f"PSI Score: {psi_score:.4f}")
    print(f"Interpretation: {interpretation}")

    if psi_score > 0.2:
        alert_message = (
            f"📈 Market Drift Alert!\n"
            f"Stock: {symbol}\n"
            f"PSI Score: {psi_score:.4f}\n"
            f"Status: {interpretation}"
        )
        send_telegram_alert(alert_message)

    return psi_score, interpretation


if __name__ == "__main__":
    stock_list = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "TATAMOTORS.NS"]

    for symbol in stock_list:
        try:
            check_stock_drift(symbol)
        except Exception as e:
            print(f"⚠️ Error checking {symbol}: {e}")
        print("-" * 40)