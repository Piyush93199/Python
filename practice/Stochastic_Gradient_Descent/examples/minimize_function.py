import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add src to the path so we can import SGD
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.optimizer import SGD

"""
Minimizing f(x, y) = x^2 + y^2 using the "Stepping Downhill" approach (SGD).

Think of this function as a giant, smooth bowl. 
Our goal is to find the bottom of the bowl starting from somewhere around the rim.
"""

def f(x_val):
    """The shape of the bowl."""
    return x_val[0]**2 + x_val[1]**2

def grad_f(x_val):
    """The direction of the steepest ascent (we walk the other way!)."""
    return np.array([2 * x_val[0], 2 * x_val[1]])

def main():
    print("Minimizing f(x, y) = x^2 + y^2 using SGD from scratch...")
    
    # Initialize SGD
    # For a deterministic function, batch_size isn't relevant unless we had noisy samples.
    # To demonstrate 'stochasticity' from data, let's also do a simple linear regression case later.
    sgd = SGD(learning_rate=0.1, epochs=50, tolerance=1e-6)
    
    # Start at [4.0, 4.0]
    initial_point = np.array([4.0, 4.0])
    
    # Minimize
    min_point = sgd.minimize(f, grad_f, initial_point)
    
    print(f"Minimum found at: {min_point}")
    print(f"Function value at minimum: {f(min_point)}")
    
    # Visualization
    history = sgd.get_history()
    
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2
    
    plt.figure(figsize=(10, 6))
    cp = plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 20), cmap='viridis')
    plt.clabel(cp, inline=1, fontsize=10)
    
    # Plot path
    plt.plot(history[:, 0], history[:, 1], 'ro-', label='SGD Path', markersize=3)
    plt.plot(initial_point[0], initial_point[1], 'go', label='Start', markersize=8)
    plt.plot(min_point[0], min_point[1], 'bx', label='End', markersize=10)
    
    plt.title('SGD path minimizing $f(x, y) = x^2 + y^2$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    output_path = os.path.join(os.path.dirname(__file__), '../examples/sgd_minimization_path.png')
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    main()
