import torch 

x = torch.tensor([1.0, 2.0, 3.0, 4.0])
print(x)
print(type(x))

x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])

y = torch.tensor([[10.0], [20.0], [30.0], [40.0], [50.0]])

print("Input (x):", x)
print("Input (y):", y)

import torch.nn as nn

model = nn.Linear(in_features=1, out_features=1)

print(model)
print("Initial weight:", model.weight)
print("Initial bias:", model.bias)

predictions = model(x)
print("Predictions before training:", predictions)
print("Actual values:", y)

loss_function = nn.MSELoss()

loss = loss_function(predictions, y)
print("Loss (error) before training:", loss.item())

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training Loop
epochs = 1000

for epoch in range(epochs):
    # Step 1: Prediction karo
    predictions = model(x)

    # Step 2: Loss calculate karo
    loss = loss_function(predictions, y)

    # Step 3: Purane gradients clear karo (important!)
    optimizer.zero_grad()

    # Step 4: Naye gradients calculate karo
    loss.backward()

    # Step 5: Weight/Bias update karo
    optimizer.step()

    # Har 20 epochs mein progress dikhao
    if epoch % 20 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

print("\n--- FINAL RESULTS ---")
print("Final weight:", model.weight.item())
print("Final bias:", model.bias.item())

# Ek naya test karo - 6000 sq ft ghar ka price predict karo (jo training data mein nahi tha)
test_input = torch.tensor([[6.0]])
predicted_price = model(test_input)
print("Predicted price for size=6:", predicted_price.item())
print("Expected price (pattern: size*10):", 60)