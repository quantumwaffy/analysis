import numpy as np


def update_matrix(matrix: np.ndarray, S: float, Cf: float, unit: str)-> np.ndarray:
    if unit == '1X&&yes':
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                if i >= j and i > 0 and j > 0:
                    matrix[i, j] = A[i, j] - S * Cf
                matrix[i, j] = A[i, j] + S
        return matrix
    if unit == '1X&&no':
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                if i < j or i == 0 or j == 0:
                    matrix[i, j] = A[i, j] - S * Cf
                matrix[i, j] = A[i, j] + S
        return matrix
    if unit == '12&&yes':
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                if i != j and i > 0 and j > 0:
                    matrix[i, j] = A[i, j] - S * Cf
                matrix[i, j] = A[i, j] + S
        return matrix
    if unit == '12&&no':
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                if i == j or i == 0 or j == 0:
                    matrix[i, j] = A[i, j] - S * Cf
                matrix[i, j] = A[i, j] + S
        return matrix
    if unit == '2X&&yes':
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                if i <= j and i > 0 and j > 0:
                    matrix[i, j] = A[i, j] - S * Cf
                matrix[i, j] = A[i, j] + S
        return matrix
    if unit == '2X&&no':
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                if i > j or i == 0 or j == 0:
                    matrix[i, j] = A[i, j] - S * Cf
                matrix[i, j] = A[i, j] + S
        return matrix
    else:
        return 'Incorrect unit'


#Testing

A = np.zeros((5, 5), dtype=float)
print('Initial matrix:\n', A, '\n')

print('1X&&yes:\n', update_matrix(A, 2.0, 3.0, '1X&&yes'), '\n')
print('1X&&no:\n', update_matrix(A, 2.0, 3.0, '1X&&no'), '\n')
print('12&&yes:\n', update_matrix(A, 2.0, 3.0, '12&&yes'), '\n')
print('12&&no:\n', update_matrix(A, 2.0, 3.0, '12&&no'), '\n')
print('2X&&yes:\n', update_matrix(A, 2.0, 3.0, '2X&&yes'), '\n')
print('2X&&no:\n', update_matrix(A, 2.0, 3.0, '2X&&no'), '\n')
print('3X&&no:\n', update_matrix(A, 2.0, 3.0, '3X&&no'), '\n')





