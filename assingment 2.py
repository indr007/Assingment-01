import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(4, 2)

print(newarr)
print(newarr[[1,1,2,2],[0,1,0,1]])



