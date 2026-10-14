import torch
import torch.nn as nn
import mlflow
import mlflow.pytorch

# ===== MLflow Experiment Start Karo =====
mlflow.set_experiment("house_price_predictor")

with mlflow.start_run():
    
    # ===== Hyperparameters (training settings) =====
    learning_rate = 0.01
    epochs = 200

    # MLflow ko batao ye settings kya thi
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("epochs", epochs)

    # ===== Data =====
    X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
    y = torch.tensor([[10.0], [20.0], [30.0], [40.0], [50.0]])

    # ===== Model Setup =====
    model = nn.Linear(in_features=1, out_features=1)
    loss_function = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    # ===== Training Loop =====
    for epoch in range(epochs):
        predictions = model(X)
        loss = loss_function(predictions, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Har 20 epochs mein loss ko MLflow mein bhi log karo
        if epoch % 20 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
            mlflow.log_metric("loss", loss.item(), step=epoch)

    # Final loss bhi log karo
    mlflow.log_metric("final_loss", loss.item())

    # Model ko bhi save karo MLflow ke through
mlflow.pytorch.log_model(model, "model", input_example=X.numpy())

print("\nTraining complete! Check MLflow UI for details.")