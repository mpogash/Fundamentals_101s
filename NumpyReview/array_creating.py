"""
M. Pogash 2026-06-05

numpy 101
"""

# == IMPORT LIBS ========================
import numpy as np
from print_np_array_stats import print_np_array_stats

# == 1D ARRAY CREATION ====================
# create 1D array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print_np_array_stats(arr1,"arr1")

# create 2D array
# -- notice the [[ ]] within np.array that is unique to 2D
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print_np_array_stats(arr2,"np.array([[1, 2, 3],\n[4, 5, 6],\n[7, 8, 9]])")

# create column array
arr1_col = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
print_np_array_stats(arr1_col,"np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])")

# create zeroes 1D array
arr1_z = np.zeros(5,)
print_np_array_stats(arr1_z,"np.zeros(5,)")

# create zeroes 2D array
# -- note the (( ))
arr2_z = np.zeros((3,3))
print_np_array_stats(arr2_z,"np.zeros((3,3))")

# create ones 1D array
arr1_o = np.ones(5,)
print_np_array_stats(arr1_o,"np.ones(5,)")

# create empty 1D array
arr1_e = np.empty(5,)
print_np_array_stats(arr1_e,"np.empty(5,)")

# create random 1D array
arr1_r = np.random.random(5,)
print_np_array_stats(arr1_r,"np.random.random(5,)")

# create random 1D array
arr1_r = np.random.random(5,)
print_np_array_stats(arr1_r,"np.random.random(5,)")

# create array of evenly spaced values, specify step size
arr1_ar = np.arange(0,10,3)
print_np_array_stats(arr1_ar,"np.arange(0,10,3)")

# create array of evenly spaced values, specify step size
arr1_ls = np.linspace(10,20,3)
print_np_array_stats(arr1_ls,"np.linspace(10,20,3)")

# create array of evenly spaced values, specify step size
arr2_ar_re = np.arange(0,9,1).reshape(3,3)
print_np_array_stats(arr2_ar_re,"np.arange(0,9,1).reshape(3,3)")




