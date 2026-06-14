"""
M. Pogash 2026-06-05

numpy 101
"""

# == IMPORT LIBRARIES ====================
import numpy as np
from print_np_array_stats import print_np_array_stats


# == ARRAY CREATION ====================
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# == ARRAY OPERATIONS ==================
arr1_sum = arr1+100
print_np_array_stats(arr1_sum,"arr1+100")

arr1_sum2 = arr1 + 100*np.ones(arr1.shape)
print_np_array_stats(arr1_sum2,"arr1 + 100*np.ones(arr1.shape)")

# arr1_s2 = arr1 + [100, 0]
# print_np_array_stats(arr1_s2,"arr1_s2")
# ValueError: operands could not be broadcast together with shapes (9,) (2,)

arr1_square = arr1**2
print_np_array_stats(arr1_square,"arr1**2")

arr1_cubed = arr1**3
print_np_array_stats(arr1_cubed,"arr1**3")

arr1_divide = arr1 / 2
print_np_array_stats(arr1_divide," arr1 / 2")

arr1_exp = np.exp(arr1-1)
print_np_array_stats(arr1_exp," np.exp(arr1-1)")

arr1_log = np.log(arr1-1)
print_np_array_stats(arr1_log,"np.log(arr1-1)")

arr1_sin = np.sin(arr1-1)
print_np_array_stats(arr1_sin,"np.sin(arr1-1)")

arr1_cos = np.cos(arr1-1)
print_np_array_stats(arr1_log,"np.cos(arr1-1)")
