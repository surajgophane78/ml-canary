import math

result = math.sqrt(16)
print(result)

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

# Normal Python list
normal_list = [1, 2, 3, 4]
print(normal_list * 2) # Ye list ko DOUBLE karega (repeat). miltiply nahi 

#Numpy_array 
numpy_array = np.array([1, 2, 3, 4])
print(numpy_array * 2) #Ye har ELEMENT ko multiply 

data = np.array([10, 20, 30, 40, 50])


print("Mean (average):", np.mean(data))
print("Standard Deviation:", np.std(data))
print("Max value:", np.max(data))
print("Min value:", np.min(data))
