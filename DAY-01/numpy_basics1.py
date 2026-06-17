# QUESTION1: Create a NumPy array containing numbers from 1 to 20 and find:
# - Mean    
# - Median    
# - Standard Deviation

import numpy as np

arr = np.arange(1, 21)
print(arr)

mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

print("Array:", arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)

# Question 2: Given a 3×3 matrix:
#  - Find its transpose.    
# - Find the sum of each row and each column.

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Approach
# Create array using np.arange()
# Use np.mean()
# Use np.median()
# Use np.std()

# output:
# Mean = 10.5
# Median = 10.5
# Standard Deviation ≈ 5.77

# ML Use:
# Data analysis
# Feature scaling
# Understanding data distribution