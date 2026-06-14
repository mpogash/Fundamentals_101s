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

# == 1D ARRAY OPERATIONS ==================
print(f"arr1[0:3] is {arr1[0:3]}")
print(f"arr1[:3] is {arr1[:3]}")
print(f"arr1[6:] is {arr1[6:]}")
print(f"arr1[2:4] is {arr1[2:4]}")
print(f"arr1[::2] is {arr1[::2]}")
print(f"arr1[::-1] is {arr1[::-1]}")
print('\n')

# == 2D ARRAY OPERATIONS ==================
print(f"arr2[0:2] is {arr2[0:2]}")
print(f"arr2[:2] is {arr2[:2]}")
print(f"arr2[6:] is {arr2[6:]}")
print(f"arr2[2:4] is {arr2[2:4]}")
print(f"arr2[::2] is {arr2[::2]}")
print(f"arr2[::-2] is {arr2[::-2]}")
print(f"arr2[1,:] is {arr2[1,:]}")
print(f"arr2[:,1] is {arr2[:,1]}")
print(f"arr2[:,::-1] is {arr2[:,::-1]}")
print(f"arr2[::-1,:] is {arr2[::-1,:]}")
print(f"arr2[::-1] is {arr2[::-1]}")
print(f"arr2[[0, 1],[1, 2]] is {arr2[[0, 1],[1, 2]]}")
print(f"arr2[[0, 1],:] is {arr2[[0, 1],:]}")
print(f"arr2[:,[0, 1]] is {arr2[:,[0, 1]]}")



"""
# == 2D ARRAY OPERATIONS ==================
print(f"arr2[0] is {arr2[0]}")
print(f"arr2[1] is {arr2[1]}")
print(f"arr2[2] is {arr2[2]}")
print(f"arr2[-1] is {arr2[-1]}")
print(f"arr2[-2] is {arr2[-2]}")

# == 2D ARRAY OPERATIONS ==================
print(f"arr2[0,0] is {arr2[0,0]}")
print(f"arr2[0,1] is {arr2[0,1]}")
print(f"arr2[1,0] is {arr2[1,0]}")
print(f"arr2[-1,0] is {arr2[-1,0]}")
print(f"arr2[-1,-1] is {arr2[-1,-1]}")

"""