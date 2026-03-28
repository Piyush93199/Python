# Stochastic Gradient Descent (SGD) from Scratch

This project implements the **Stochastic Gradient Descent (SGD)** optimization algorithm from scratch in Python using only `numpy` for computations and `matplotlib` for visualization.

## Overview

Stochastic Gradient Descent is a fundamental optimization algorithm used in Machine Learning. Unlike standard Gradient Descent, which uses the entire dataset to compute the gradient for a single update, SGD (and its mini-batch variation) updates parameters using only a subset of the data, introducing noise that can help escape local minima and speed up convergence.

### Features
- **Deterministic Optimization**: Minimize standard mathematical functions (e.g., $f(x, y) = x^2 + y^2$).
- **Stochastic Optimization**: Solve Linear Regression by updating on single data points.
- **Visualizations**: Plots the optimization path for convex functions and the linear regression line for data-based optimization.

## 🧠 How It Works (The Logic)

Imagine you're standing on a foggy mountain and want to find the lowest valley. You can't see the bottom, so you have to feel the slope under your feet.

1.  **Start at a Random Spot**: Pick a starting point for your search.
2.  **Shuffle the Deck**: Mix up your data points so the algorithm doesn't get "stuck" on a specific pattern.
3.  **Look Locally**: Instead of checking the whole mountain, look at a small patch (a "mini-batch") and see which way is downhill.
4.  **Step Forward**: Take a small, careful step in that direction (controlled by your "learning rate").
5.  **Repeat**: Keep stepping until the ground feels flat or you've run enough rounds.

## File Structure

```text
Stochastic_Gradient_Descent/
├── src/
│   └── optimizer.py         # core SGD implementation
├── examples/
│   ├── minimize_function.py # function minimization example
│   └── linear_regression.py # LR with SGD example
├── data/
│   └── .gitkeep             # data directory placeholder
├── requirements.txt         # project dependencies
├── .gitignore               # python-specific gitignore
└── README.md                # project documentation
```

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd Stochastic_Gradient_Descent
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Simple Function Minimization
Find the minimum of $f(x, y) = x^2 + y^2$:
```bash
python examples/minimize_function.py
```
This script will output the found minimum and save a plot of the optimization path at `examples/sgd_minimization_path.png`.

### 2. Linear Regression with SGD
Perform linear regression on synthetic data using stochastic updates (batch_size=1):
```bash
python examples/linear_regression.py
```
This script will output the regression coefficients and save a plot of the result at `examples/linear_regression_sgd.png`.

## Core Implementation

The `SGD` class in `src/optimizer.py` provides a generic interface:

```python
sgd = SGD(learning_rate=0.01, epochs=100, batch_size=1)
min_point = sgd.minimize(objective_func, gradient_func, initial_point, data=my_data)
```

## License
MIT
