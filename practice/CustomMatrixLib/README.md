# Custom Matrix Operations Library 🧮

A Python-based repository of fundamental linear algebra operations. This project implements core matrix manipulations from scratch using **NumPy indexing** without relying on built-in high-level methods like `.T`, `np.dot()`, or the `@` operator.

## 🚀 Overview
As a Computer Science student, understanding the underlying mechanics of matrix operations is crucial for fields like **Machine Learning** and **Data Science**. This library serves as a deep dive into the algorithmic complexity and memory management involved in linear algebra.

## ✨ Features
* **Manual Transposition**: Implementation of row-to-column swapping logic ($A_{ij} \to A_{ji}$).
* **Matrix Multiplication**: A pure Python implementation of the dot product using $O(n^3)$ nested loops.
* **Error Handling**: Robust validation for matrix dimension compatibility.
* **Unit Tested**: Verified against official NumPy outputs to ensure 100% mathematical accuracy.

## 📁 Project Structure
```text
CustomMatrixLib/
├── src/
│   └── matrix_operations.py  # Core logic and custom functions
├── tests/
│   └── test_operations.py    # Automated test suite using unittest
├── .gitignore                # Files to ignore in Git
└── README.md                 # Project documentation
```

## 🛠️ Usage

```python
import numpy as np
from src.matrix_operations import CustomMatrixLib

# Initialize the library
lib = CustomMatrixLib()

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Perform operations
transposed = lib.transpose(A)
product = lib.multiply(A, B)

print("Product:\n", product)
```

## 🧪 Running Tests

To verify the implementation against NumPy's native methods, run the following command:

```bash
python3 tests/test_operations.py
```

## 📈 Complexity Analysis

| Operation | Algorithm | Time Complexity |
| :--- | :--- | :--- |
| Transpose | Nested Loop | $O(m \times n)$ |
| Multiplication | Triple Nested Loop | $O(n^3)$ |
