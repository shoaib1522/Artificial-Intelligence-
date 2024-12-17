def calculate_mean(values):
    total = sum(values)
    return total / len(values)

def calculate_slope(X, Y, mean_X, mean_Y):
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(len(X)))
    return numerator / denominator

def calculate_intercept(mean_X, mean_Y, slope):
    return mean_Y - slope * mean_X

def predict(X, theta_0, theta_1):
    return [theta_0 + theta_1 * x for x in X]

def calculate_mse(Y, Y_pred):
    errors = [(Y[i] - Y_pred[i]) ** 2 for i in range(len(Y))]
    return sum(errors) / len(errors)


def fit_linear_regression(X, Y):
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)
    slope = calculate_slope(X, Y, mean_X, mean_Y)
    intercept = calculate_intercept(mean_X, mean_Y, slope)
    return intercept, slope


X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 7, 8]

theta_0, theta_1 = fit_linear_regression(X, Y)

Y_pred = predict(X, theta_0, theta_1)

mse = calculate_mse(Y, Y_pred)

print(f"Slope (theta_1): {theta_1}")
print(f"Intercept (theta_0): {theta_0}")
print(f"Mean Squared Error (MSE): {mse}")
