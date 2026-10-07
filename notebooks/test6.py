import sys
sys.path.append("src")   # ye line batati hai Python ko "src" folder mein bhi dhundo

from drift_detector import DriftDetector
import numpy as np

reference_marks = np.random.normal(loc=70, scale=10, size=200)

detector = DriftDetector(reference_marks)

print("Bins created:", detector.bins)
print("Number of bins:", detector.num_bins)