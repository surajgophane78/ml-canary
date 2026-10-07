import sys
sys.path.append("src")   # ye line batati hai Python ko "src" folder mein bhi dhundo

from drift_detector import DriftDetector
import numpy as np

reference_marks = np.random.normal(loc=70, scale=10, size=200)

detector = DriftDetector(reference_marks)

print("Bins created:", detector.bins)
print("Number of bins:", detector.num_bins)

live_marks = np.random.normal(loc=50, scale=10, size=200)

psi_score = detector.calculate_psi(live_marks)
print("PSI Score:", psi_score)

message = detector.interpret_psi(psi_score)
print("Interpretation:", message)
