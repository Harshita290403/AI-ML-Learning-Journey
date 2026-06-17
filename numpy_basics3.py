# OUESTION 3:
# Create two NumPy arrays and perform: 
# - Element-wise addition   
# - Element-wise multiplication    
# - Dot Product

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

addition = a + b

print(addition)

multiplication = a * b

print(multiplication)

dot_product = np.dot(a,b)

print(dot_product)

# output:
# addition- [5 7 9]
# multiplicationn- [ 4 10 18 ]
# dot product- 32