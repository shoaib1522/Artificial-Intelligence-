def calculate_mean(values):
    total = 0
    for value in values:
        total += value
    mean = total / len(values)
    return mean

def calculate_slope(X, Y, mean_X, mean_Y):
    numerator = 0
    for i in range(len(X)):
        numerator += (X[i] - mean_X) * (Y[i] - mean_Y)
    denominator = 0
    for i in range(len(X)):
        denominator += (X[i] - mean_X) ** 2
    slope = numerator / denominator
    return slope

def calculate_intercept(mean_X, mean_Y, slope):
    intercept = mean_Y - slope * mean_X
    return intercept

def predict(X, theta_0, theta_1):
    predictions = []
    for x in X:
        y_pred = theta_0 + theta_1 * x
        predictions.append(y_pred)
    return predictions

def calculate_mse(Y, Y_pred):
    errors = []
    for i in range(len(Y)):
        error = (Y[i] - Y_pred[i]) ** 2
        errors.append(error)
    total_error = 0
    for error in errors:
        total_error += error
    mse = total_error / len(Y)
    return mse

def gradient_descent(X, Y, theta_0, theta_1, learning_rate, iterations):
    for _ in range(iterations):
        sum_error_theta_0 = 0
        sum_error_theta_1 = 0
        for i in range(len(X)):
            prediction = theta_0 + theta_1 * X[i]
            error = Y[i] - prediction
            sum_error_theta_0 += -2 * error
            sum_error_theta_1 += -2 * error * X[i]
        d_theta_0 = sum_error_theta_0 / len(X)
        d_theta_1 = sum_error_theta_1 / len(X)
        theta_0 = theta_0 - learning_rate * d_theta_0
        theta_1 = theta_1 - learning_rate * d_theta_1
    return theta_0, theta_1

def fit_linear_regression(X, Y, learning_rate=0.01, iterations=1000):
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)
    theta_1 = calculate_slope(X, Y, mean_X, mean_Y)
    theta_0 = calculate_intercept(mean_X, mean_Y, theta_1)
    theta_0, theta_1 = gradient_descent(X, Y, theta_0, theta_1, learning_rate, iterations)
    return theta_0, theta_1

def test_model():
    X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000]
    learning_rate = 0.01
    iterations = 1000
    theta_0, theta_1 = fit_linear_regression(X, Y, learning_rate, iterations)
    Y_pred = predict(X, theta_0, theta_1)
    mse = calculate_mse(Y, Y_pred)
    print("Slope (theta_1):", theta_1)
    print("Intercept (theta_0):", theta_0)
    print("Mean Squared Error (MSE):", mse)
    print("Predicted Values:", Y_pred)

test_model()
