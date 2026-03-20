import numpy as np

class CustomMatrixLib:
    """
    A repository of manual matrix operations using basic indexing.
    Designed to demonstrate the underlying logic of Linear Algebra.
    """
    
    @staticmethod
    def transpose(matrix):
        """
        Manually flips a matrix over its diagonal.
        Logic: The element at row 'i', col 'j' moves to row 'j', col 'i'.
        """
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix)
            
        rows, cols = matrix.shape
        result = np.zeros((cols, rows))
        
        for i in range(rows):
            for j in range(cols):
                result[j, i] = matrix[i, j]
        return result

    @staticmethod
    def multiply(A, B):
        """
        Performs matrix multiplication (Dot Product).
        Complexity: O(n^3) using nested loops.
        """
        if not (isinstance(A, np.ndarray) and isinstance(B, np.ndarray)):
            A, B = np.array(A), np.array(B)

        rows_A, cols_A = A.shape
        rows_B, cols_B = B.shape

        if cols_A != rows_B:
            raise ValueError(f"Dimension Mismatch: A cols({cols_A}) != B rows({rows_B})")

        result = np.zeros((rows_A, cols_B))

        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i, j] += A[i, k] * B[k, j]
        return result