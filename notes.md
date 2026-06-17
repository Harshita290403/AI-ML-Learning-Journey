1)WHAT IS NumPy?
. It is a python library
. Used for fast mathematical calculation
. Used for Working with arrays and matrices
. used for Data preprocessing for ML
. used for Linear algebra operations

2)NumPy Arrays vs Python Lists:

"Python List "             "NumPy Array"
.slower                     .faster
.more memory                .less memory
.Limited math operations    .Supports vectorized operations
.general data               .ML/data science

3)ARRAY CREATION AND INDEXING:

import numpy as np

arr = np.array([10,20,30,40])

print(arr[0])
print(arr[2])

here array is created using [] and indexing is what position it is ,its starts with zero
->OUTPUT:-
10
30

4)BASIC OPERATIONS:
arr = np.array([1,2,3])

print(arr + 2)
print(arr * 2)

Here +2 gets added to every no. in the index like 1+2=3 and so on and jst like that 1*2=2 and so on

->OUPUT
[3 4 5]
[2 4 6]

5)BROADCASTING:
arr = np.array([1,2,3])

print(arr + 10)

->OUTPUT:
[11 12 13]

Broadcasting automatically applies the value to every element.