import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cross_entropy_loss(y_true, y_pred):
    m = len(y_true)
    loss = -1 / m * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

def gradient_descent(X, y, weights, learning_rate, iterations):
    m = X.shape[0]
    losses = []

    for i in range(iterations):
        z = np.dot(X, weights)
        y_pred = sigmoid(z)
        gradient = np.dot(X.T, (y_pred - y)) / m
        weights -= learning_rate * gradient
        loss = cross_entropy_loss(y, y_pred)
        losses.append(loss)

        if i % 100 == 0:
            print(f"Iteration {i}, Loss: {loss:.4f}")

    return weights, losses

def predict(X, weights):
    z = np.dot(X, weights)
    y_pred = sigmoid(z)
    return (y_pred >= 0.5).astype(int)

def evaluate(y_true, y_pred):
    accuracy = np.mean(y_true == y_pred)
    return accuracy

def logistic_regression(X, y, learning_rate=0.01, iterations=1000):
    X = np.c_[np.ones(X.shape[0]), X]
    weights = np.zeros(X.shape[1])
    weights, losses = gradient_descent(X, y, weights, learning_rate, iterations)
    return weights, losses

def plot_decision_boundary(X, y, weights):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', alpha=0.7)
    x1_min, x1_max = X[:, 0].min(), X[:, 0].max()
    x2_min, x2_max = X[:, 1].min(), X[:, 1].max()
    xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max, 100),
                           np.linspace(x2_min, x2_max, 100))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    grid = np.c_[np.ones(grid.shape[0]), grid]
    probs = sigmoid(np.dot(grid, weights)).reshape(xx1.shape)
    plt.contourf(xx1, xx2, probs, levels=[0, 0.5, 1], alpha=0.2, colors=['blue', 'red'])
    plt.title("Decision Boundary")
    plt.xlabel("Feature 1 (X1)")
    plt.ylabel("Feature 2 (X2)")
    plt.show()

if __name__ == "__main__":
    X = np.array([[0.1, 1.1],
                  [1.2, 0.9],
                  [1.5, 1.6],
                  [2.0, 1.8],
                  [2.5, 2.1],
                  [0.5, 1.5],
                  [1.8, 2.3],
                  [0.2, 0.7],
                  [1.9, 1.4],
                  [0.8, 0.6]])

    y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 0])

    mean = X.mean(axis=0)
    std = X.std(axis=0)
    X_normalized = (X - mean) / std

    plt.scatter(X_normalized[:, 0], X_normalized[:, 1], c=y, cmap='bwr', alpha=0.7)
    plt.title("Data Visualization")
    plt.xlabel("Feature 1 (X1)")
    plt.ylabel("Feature 2 (X2)")
    plt.show()

    learning_rate = 0.1
    iterations = 1000
    weights, losses = logistic_regression(X_normalized, y, learning_rate, iterations)

    plt.plot(range(iterations), losses)
    plt.title("Loss Curve")
    plt.xlabel("Iterations")
    plt.ylabel("Cross-Entropy Loss")
    plt.show()

    X_with_intercept = np.c_[np.ones(X_normalized.shape[0]), X_normalized]
    y_pred = predict(X_with_intercept, weights)
    accuracy = evaluate(y, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    plot_decision_boundary(X_normalized, y, weights)
