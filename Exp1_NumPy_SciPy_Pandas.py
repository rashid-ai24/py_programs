import numpy as np
from scipy import special
import pandas as pd

# NumPy Example
arr = np.array([[1, 2, 3], [4, 2, 5]])
print("Array is of type:", type(arr))
print("No. of dimensions:", arr.ndim)
print("Shape of array:", arr.shape)
print("Size of array:", arr.size)
print("Array stores elements of type:", arr.dtype)

# SciPy Example
a = special.exp10(3)
print(a)
b = special.exp2(3)
print(b)
c = special.sindg(90)
print(c)
d = special.cosdg(45)
print(d)

# Pandas Example
data = pd.DataFrame({
    "x1": ["y", "x", "y", "x", "x", "y"],
    "x2": range(16, 22),
    "x3": range(1, 7),
    "x4": ["a", "b", "c", "d", "e", "f"],
    "x5": range(30, 24, -1)
})
print(data)

s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame({'first': s1, 'second': s2, 'third': s3})
print(df)
