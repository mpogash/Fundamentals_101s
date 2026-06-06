"""
M. Pogash 2026-06-05

to learn numpy

"""

# == IMPORT LIBRARIES ====================
import numpy as np
from print_np_array_stats import print_np_array_stats
from print_np_array_stats_short import print_np_array_stats_short

# == CREATE ARRAY ===========================
arr1 = np.arange(0,9,1)

# == CONCATENATE 1D ARRAYS ==================
arr2 = np.concatenate((arr1,arr1))
print_np_array_stats_short(arr2,"np.concatenate((arr1,arr1))")

arr2 = np.concatenate((arr1,arr1),axis=0)
print_np_array_stats_short(arr2,"np.concatenate((arr1,arr1),axis=0)")

#arr1 = np.arange(0,9,1)
#arr2 = np.concatenate((arr1,arr1),axis=1)
print(f"cannot np.concatenate((arr1,arr1),axis=1)")

# horizontal stack
arr2 = np.hstack((arr1,arr1))
print_np_array_stats_short(arr2,"np.hstack((arr1,arr1))")

# vertical stack
arr2 = np.vstack((arr1,arr1))
print_np_array_stats_short(arr2,"np.vstack((arr1,arr1))")

# row stack
arr2 = np.r_[arr1,arr1]
print_np_array_stats_short(arr2,"np.r_[arr1,arr1]")

# column stack
arr2 = np.column_stack((arr1,arr1))
print_np_array_stats_short(arr2,"np.column_stack((arr1,arr1))")

# column stack
arr2 = np.c_[arr1,arr1]
print_np_array_stats_short(arr2,"np.c_[arr1,arr1]")


