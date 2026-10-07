import numpy as np

reference_marks = np.random.normal(loc=70, scale=10, size=200)
live_marks = np.random.normal(loc=50, scale=10, size=200)

print("Referance data sample:", reference_marks[:5])
print("Live data sample:", live_marks[:5])

bins = np.linspace(0, 100, 11)
print("Bins:", bins)


ref_counts, _ = np.histogram(reference_marks, bins=bins)
print("reference counts per bin:", ref_counts)

live_counts, _ = np.histogram(live_marks, bins=bins)
print("Live counts per bin:", live_counts)

ref_percent = ref_counts / len(reference_marks)
live_percent = live_counts / len(live_marks)

print("Referance %:", ref_percent)
print("Live %:", live_percent)


ref_percent = np.where(ref_percent == 0, 0.0001, ref_percent)
live_percent = np.where(live_percent == 0, 0.0001, live_percent)

print("Reference % (fixed):", ref_percent)
print("Live % (fixed):", live_percent)

psi_values = (live_percent - ref_percent) * np.log(live_percent / ref_percent)

print("PSI per bin:", psi_values)

psi_total = np.sum(psi_values)
print("\n🎯 FINAL PSI SCORE:", psi_total)
