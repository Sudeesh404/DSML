import numpy as np

#initializing 2 arrays
a1 = np.array([3,6,9,12])
a2 = np.array([2,4,6,8])

#sum of arrays
Sum = np.add(a1,a2)
print(Sum)

#product of arrays
Prod = np.multiply(a1,a2)
print(Prod)

#mean
mean = np.mean(Sum)

#max value in Prod
max_val = np.max(Prod)
print(max_val)
