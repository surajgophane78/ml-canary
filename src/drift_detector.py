import numpy as np

class DriftDetector:
    def __init__(self, reference_data, num_bins=10):
        self.reference_data = reference_data
        self.num_bins = num_bins
        self.bins = np.linspace(min(reference_data), max(reference_data), num_bins + 1)

    def calculate_psi(self, live_data):
        ref_counts, _ = np.histogram(self.reference_data, bins=self.bins)
        live_counts, _ = np.histogram(live_data, bins=self.bins)

        ref_percent = ref_counts / len(self.reference_data)
        live_percent = live_counts / len(live_data)

        ref_percent = np.where(ref_percent == 0, 0.0001, ref_percent)
        live_percent = np.where(live_percent == 0, 0.0001, live_percent)

        psi_values = (live_percent - ref_percent) * np.log(live_percent / ref_percent)
        psi_total = np.sum(psi_values)

        return psi_total 
          
    def interpret_psi(self, psi_score):
        if psi_score < 0.1:
            return "No significant drift"
        elif psi_score < 0.2:
            return "Moderate drift - monitor closely"
        else:
            return "Major drift detected - action required!"
        