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

# == USING WHERE ============================
# This works as expected
arr2_sum_ax1_filter = arr2.sum(where=arr2>6)
print_np_array_stats(arr2_sum_ax1_filter,"arr2.sum(where=arr2>6)")
# sum is a reduction function. It takes an array and reduces it down to a single scalar value.
# when a where condition is passed to sum, numpy automatically knows what the "safe" default starting
# value should be, 0

# This does not work as expected 
arr1_multiply_filt = np.multiply(arr1,2,where=arr1>6)
print_np_array_stats(arr1_multiply_filt,"np.multiply(arr1,2,where=arr1>6)")
# np.multiply tells numpy to
#  1. create a brand new empty output array of the appropiate size on the RAM, 9 elements
#  2. where arr1 > 6 is True, calculate the multiplication and place it in the array
#  3. where arr1 > 6 is False, do nothing...
# numpy created a fresh block of memory for the output, but, the memory wasn't wiped, so, 
# doing nothing leaves the original values that were previously in memory 

arr1_multiply_filt_ic = np.multiply(arr1,2,where=arr1>6,out=None)
print_np_array_stats(arr1_multiply_filt_ic,"np.multiply(arr1,2,where=arr1>6)")
# this does the samething as above

arr1_multiply_filt_c = np.zeros(arr1.shape)
np.multiply(arr1,2,where=arr1>6,out=arr1_multiply_filt_c)
print_np_array_stats(arr1_multiply_filt_c,"np.multiply(arr1,2,where=arr1>6)")
# now, we filled the output array with 0s first and then populated it

arr1_multiply_filt_c2 = arr1.copy()
arr1_multiply_filt_c2[arr1_multiply_filt_c2 > 6] *= 2
print_np_array_stats(arr1_multiply_filt_c2,"arr1_multiply_filt_c2 = arr1.copy(); arr1_multiply_filt_c2[arr1_multiply_filt_c2 > 6] *= 2")
# here we created a deep copy 