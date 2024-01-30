import numpy as np
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[2, 2], [4, 4], [6, 6]])
def matrix_multiply(matrix_a, matrix_b):
    shape_a = matrix_a.shape
    shape_b = matrix_b.shape
    if len(shape_a) == len(shape_b) and shape_a[1] == shape_b[0]:
        result = np.dot(matrix_a, matrix_b)
        return result
    else:
        print("Error: The dimensions of the matrices are not compatible for multiplication.")
print(matrix_multiply(matrix_a, matrix_b))
