import math

def euclidean_distance(a, b):
    if len(a) != len(b):
        raise ValueError("Points must have the same number of coordinates")

    dist_squared = sum((x - y) ** 2 for x, y in zip(a, b))
    return math.sqrt(dist_squared)

# Test the function
x = [2, 9, 9]
y = [1, 4, 3]
try:
    distance = euclidean_distance(x, y)
    print("The distance between the two points is", distance)
except ValueError as e:
    print(e)
