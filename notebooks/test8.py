import torch
import torch.nn as nn
import numpy as np
import sys
sys.path.append("src")
from drift_detector import DriftDetector

x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([[10.0], [20.0], [30.0], [40.0], [50.0]])

model = nn.Linear(in_features=1, out_features=1)
loss_function = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(200):
    predictions = model(x)
    loss = loss_function(predictions, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Model training complete! Final weight:", model.weight.item())


# ===== TRAINING DATA KO "REFERENCE DATA" BANAO =====
reference_data = x.numpy().flatten()
print("\nReference data (house sizes model trained on):", reference_data)

live_data = np.array([8.0, 9.0, 10.0, 11.0, 12.0, 8.5, 9.5, 10.5])

print("\nLive data (what users are checking now):", live_data)

# ===== DRIFT CHECK KARO =====
detector = DriftDetector(reference_data, num_bins=5)

psi_score = detector.calculate_psi(live_data)
interpretation = detector.interpret_psi(psi_score)

print("\n===== DRIFT DETECTION REPORT =====")
print(f"PSI Score: {psi_score:.4f}")
print(f"Interpretation: {interpretation}")