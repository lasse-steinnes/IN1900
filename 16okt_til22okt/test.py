import numpy as np

arr = np.array([1,1,-1,-2,-3,4,5])

result = []
for i, v in enumerate(arr):
    if i < 3:
        result.append('True')
    else:
        result.append(v)

print(result)
