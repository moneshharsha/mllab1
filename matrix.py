import numpy as np

a = np.array([[2, 4, 6], [1, 3, 5]])

def trans(a):
    return np.array([list(row) for row in zip(*a)])

print("Original Matrix")
print(a)
print("Transpose")
print(trans(a))
