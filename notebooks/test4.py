import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

reference_marks = np.random.normal(loc=70, scale=10, size=200)

live_marks = np.random.normal(loc=50, scale=10, size=200)


plt.hist(reference_marks, bins=20, alpha=0.5, label="Reference Data")
plt.hist(live_marks, bins=20, alpha=0.5, label="Live Data")
plt.legend()
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Reference vs Live Data Distribution")
plt.show()