import numpy as np
import matplotlib.pyplot as plt

# Step 1: Dataset Setup
X = np.array([
    [0.1, 0.6],
    [0.15, 0.71],
    [0.25, 0.8],
    [0.35, 0.45],
    [0.5, 0.5],
    [0.6, 0.2],
    [0.65, 0.3],
    [0.8, 0.35]
])
y = np.array([1, 1, 1, 1, 0, 0, 0, 0]).reshape(-1, 1)

# Step 2: Initialize weights and biases
def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(42)  # For reproducibility
    W1 = np.random.randn(input_size, hidden_size) * 0.01
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size) * 0.01
    b2 = np.zeros((1, output_size))
    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

# Step 3: Implement forward propagation
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def forward_propagation(X, parameters):
    W1, b1 = parameters["W1"], parameters["b1"]
    W2, b2 = parameters["W2"], parameters["b2"]

    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache

# Step 4: Compute the loss
def compute_loss(y_true, y_pred):
    m = y_true.shape[0]
    loss = -np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)) / m
    return loss

# Step 5: Implement backward propagation
def backward_propagation(X, y, parameters, cache):
    m = X.shape[0]
    W2 = parameters["W2"]
    
    A1, A2 = cache["A1"], cache["A2"]
    Z1 = cache["Z1"]

    dZ2 = A2 - y
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m
    
    dZ1 = np.dot(dZ2, W2.T) * A1 * (1 - A1)
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    gradients = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
    return gradients

# Step 6: Update weights
def update_parameters(parameters, gradients, learning_rate):
    parameters["W1"] -= learning_rate * gradients["dW1"]
    parameters["b1"] -= learning_rate * gradients["db1"]
    parameters["W2"] -= learning_rate * gradients["dW2"]
    parameters["b2"] -= learning_rate * gradients["db2"]
    return parameters

# Step 7: Training loop
def train_network(X, y, hidden_size, learning_rate, epochs):
    input_size = X.shape[1]
    output_size = 1
    
    parameters = initialize_parameters(input_size, hidden_size, output_size)

    for epoch in range(epochs):
        y_pred, cache = forward_propagation(X, parameters)
        loss = compute_loss(y, y_pred)
        gradients = backward_propagation(X, y, parameters, cache)
        parameters = update_parameters(parameters, gradients, learning_rate)

        if (epoch + 1) % 100 == 0 or epoch == 0:
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")

    return parameters

# Step 8: Plot decision boundary
def plot_decision_boundary(X, y, parameters):
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    grid = np.c_[xx.ravel(), yy.ravel()]
    probs, _ = forward_propagation(grid, parameters)
    
    Z = probs.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y.ravel(), edgecolor='k', cmap=plt.cm.Spectral)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.title("Decision Boundary")
    plt.show()

# Training the network
hidden_size = 4
learning_rate = 0.1
epochs = 1000
parameters = train_network(X, y, hidden_size, learning_rate, epochs)

# Visualizing the decision boundary
plot_decision_boundary(X, y, parameters)
