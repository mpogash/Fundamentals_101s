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
arr1_sum = arr1.sum()
print_np_array_stats(arr1_sum,"arr1.sum()")

arr2_sum = arr2.sum()
print_np_array_stats(arr2_sum,"arr2.sum()")

arr2_sum_ax0 = arr2.sum(axis=0)
print_np_array_stats(arr2_sum_ax0,"arr2.sum(axis=0)")

arr2_sum_ax1 = arr2.sum(axis=1)
print_np_array_stats(arr2_sum_ax1,"arr2.sum(axis=1)")

arr2_sum_ax1_filter = arr2.sum(where=arr2>6)
print_np_array_stats(arr2_sum_ax1_filter,"arr2.sum(where=arr2>6)")

arr1_cumsum = arr1.cumsum()
print_np_array_stats(arr1_cumsum,"arr1.cumsum()")

arr2_cumsum = arr2.cumsum()
print_np_array_stats(arr2_cumsum,"arr2.cumsum()")

arr2_cumsum_ax0 = arr2.cumsum(axis=0)
print_np_array_stats(arr2_cumsum_ax0,"arr2.cumsum(axis=0)")

arr2_cumsum_ax1 = arr2.cumsum(axis=1)
print_np_array_stats(arr2_cumsum_ax1,"arr2.cumsum(axis=1)")

arr1_min = arr1.min()
print_np_array_stats(arr1_min,"arr1.min()")

arr2_min = arr2.min()
print_np_array_stats(arr2_min,"arr2.min()")

arr1_max = arr1.max()
print_np_array_stats(arr1_max,"arr1.max()")

arr1_median = np.median(arr1)
print_np_array_stats(arr1_median,"np.median(arr1)")

arr1_std = np.std(arr1)
print_np_array_stats(arr1_std,"np.std(arr1)")

arr1_corrcoef = np.corrcoef(arr1)
print_np_array_stats(arr1_corrcoef,"np.corrcoef(arr1)")

arr1_multiply_filt = np.multiply(arr1,2,where=arr1>6)
print(f"notice this! Bad syntax. See takeaway_findings_where")
print_np_array_stats(arr1_multiply_filt,"np.multiply(arr1,2,where=arr1>6)")