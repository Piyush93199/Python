import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add src to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.optimizer import SGD

def main():
    """
    Fitting a Line with SGD: The "Tug-of-War" Approach.
    
    Think of our data as a set of points pulling on a rubber band.
    Each point wants the line to be closer to it.
    Instead of listening to everyone at once, we listen to one point at a time 
    and adjust our line slightly to make that point happier.
    """
    print("Linear Regression with SGD (One point at a time)...")
    
    # Generate random data: y = 2x + 10 + noise
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    y = 10 + 2 * X + np.random.randn(100, 1)
    
    # Combine X and y for data pooling
    # Add bias term 1 to X
    X_b = np.c_[np.ones((100, 1)), X]
    data = np.c_[X_b, y]
    
    # Linear Regression cost function (not used directly in 'minimize' with data)
    def compute_cost(theta, data_batch):
        # f(theta) = 1/2m sum (h_theta(x) - y)^2
        X_batch = data_batch[:, :-1]
        y_batch = data_batch[:, -1:]
        m = len(y_batch)
        predictions = X_batch.dot(theta)
        errors = predictions - y_batch
        return (1 / (2 * m)) * np.sum(np.square(errors))
    
    # Gradient of MSE: (1/m) X^T (X*theta - y)
    def compute_gradient(theta, data_batch):
        X_batch = data_batch[:, :-1]
        y_batch = data_batch[:, -1:]
        m = len(y_batch)
        predictions = X_batch.dot(theta)
        errors = predictions - y_batch
        # Need to reshape theta if it's 1D for grad_f
        # theta should be (2, 1) here.
        gradient = (1 / m) * X_batch.T.dot(errors)
        return gradient.flatten()
    
    # Initialize SGD
    # Batch size 1 makes it truly 'Stochastic'
    sgd = SGD(learning_rate=0.01, epochs=200, batch_size=1, tolerance=1e-5)
    
    # Initial theta (intercept=0, slope=0)
    initial_theta = np.zeros(2)
    
    # Minimize theta
    final_theta = sgd.minimize(compute_cost, compute_gradient, initial_theta, data=data)
    
    print(f"Final theta (intercept, slope): {final_theta}")
    print(f"True values (intercept=10, slope=2)")
    
    # Plot data and regression line
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', alpha=0.5, label='Data Points')
    
    # Regression line
    x_line = np.linspace(0, 2, 10)
    y_line = final_theta[0] + final_theta[1] * x_line
    plt.plot(x_line, y_line, color='red', linewidth=3, label='SGD Linear Regression')
    
    plt.title('Linear Regression with Stochastic Gradient Descent')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    # Save plot
    output_path = os.path.join(os.path.dirname(__file__), '../examples/linear_regression_sgd.png')
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    main()
