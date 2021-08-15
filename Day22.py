# Euclidean distance
import math
x = (2, 3, 7)
y = (5, 12, 9)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ",distance)
