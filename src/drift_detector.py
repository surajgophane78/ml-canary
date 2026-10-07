import numpy as np

class DriftDetector:
    def __init__(self, reference_data, num_bins=10):
        self.reference_data = reference_data
        self.num_bins = num_bins
        self.bins = np.linspace(min(reference_data), max(reference_data), num_bins + 1)
