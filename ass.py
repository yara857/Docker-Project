# 3y - x = 100
# 6y - 3x = 100
import numpy as np
a = np.array([[4]])
b = np.array([100])
x = np.linalg.solve(a, b)
print("Big fish ratio : " ,x)
print("Small fish ratio : " ,x*3)
