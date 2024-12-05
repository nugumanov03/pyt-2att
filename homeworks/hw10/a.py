import numpy as np
import matplotlib.pyplot as plt

# Data: Weekly Hours Exercised (X) and Weekly Savings (Y)
X = np.array([1, 2, 3, 4, 5])
Y = np.array([10, 20, 30, 40, 50])

# 1. Define the Prediction Function
def predict(beta_0, beta_1, X):
    return beta_0 + beta_1 * X

# 2. Calculate the Cost Function
def cost_function(Y_pred, Y_actual):
    n = len(Y_actual)
    mse = (1 / n) * np.sum((Y_pred - Y_actual) ** 2)
    return mse

# 3. Optimize Parameters Using Gradient Descent
def gradient_descent(X, Y, beta_0, beta_1, alpha, iterations):
    n = len(Y)
    for _ in range(iterations):
        # Predictions
        Y_pred = predict(beta_0, beta_1, X)
        # Compute Gradients
        d_beta_0 = -(2 / n) * np.sum(Y - Y_pred)
        d_beta_1 = -(2 / n) * np.sum((Y - Y_pred) * X)
        # Update Parameters
        beta_0 -= alpha * d_beta_0
        beta_1 -= alpha * d_beta_1
    return beta_0, beta_1

# Initial Parameters
beta_0, beta_1 = 0, 1
alpha = 0.01
iterations = 500

# Optimize Parameters
beta_0_opt, beta_1_opt = gradient_descent(X, Y, beta_0, beta_1, alpha, iterations)

# 4. Make Predictions
X_test = [6, 10]
predictions = [predict(beta_0_opt, beta_1_opt, x) for x in X_test]

print(f"Optimized Parameters: beta_0 = {beta_0_opt:.2f}, beta_1 = {beta_1_opt:.2f}")
print(f"Predicted Savings for X=6: {predictions[0]:.2f}")
print(f"Predicted Savings for X=10: {predictions[1]:.2f}")

# 5. Visualization
plt.figure(figsize=(8, 6))
# Scatter plot of actual data
plt.scatter(X, Y, color="blue", label="Data Points")
# Best-fit line
X_fit = np.linspace(1, 5, 100)
Y_fit = predict(beta_0_opt, beta_1_opt, X_fit)
plt.plot(X_fit, Y_fit, color="red", label="Best-Fit Line")
# Labels and legend
plt.title("Weekly Savings vs Weekly Exercise")
plt.xlabel("Weekly Hours Exercised")
plt.ylabel("Weekly Savings ($)")
plt.legend()
plt.grid(True)
plt.show()
