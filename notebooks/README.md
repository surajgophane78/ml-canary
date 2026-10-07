# ML Canary 🐤

A model and data drift monitoring system built from scratch in Python.

## What is this?
This project detects **data drift** — when live/production data starts 
differing significantly from the data a model was trained on. It calculates 
the **PSI (Population Stability Index)** score to measure this drift and 
will eventually send alerts when drift is detected.

## Progress So Far
- ✅ Implemented PSI calculation from scratch using NumPy
- ✅ Built a reusable `DriftDetector` class
- 🔄 Next: FastAPI service, MLflow tracking, Docker deployment

## Tech Stack (Planned)
Python, PyTorch, FastAPI, Docker, Kubernetes, AWS, GitHub Actions, Prometheus, Grafana

## Author
Suraj Gophane — BCA Student, learning MLOps from scratch.