"""
M. Pogash 2026-06-05

numpy 101
"""

# == IMPORT LIBRARIES ====================
import numpy as np
import os
from print_np_array_stats import print_np_array_stats

# == HELP ===============================
np.info(np.arange)

# == ARRAY CREATION ====================
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


## == SAVE STRICTLY ONE NUMPY ARRAY =====
# -- note the file extension .npy
np_array_filename = "np_array.npy"
np.save(np_array_filename,arr1)
del arr1
np.load(np_array_filename)
if 'arr1' in globals():
    print(f"arr1 is {arr1}")
else:
    print("arr1 does not exist after np.load(np_array.npy)")

arr1 = np.load(np_array_filename)
if 'arr1' in globals():
    print(f"arr1 is {arr1}")
else:
    print("arr1 does not exist after arr1 = np.load(np_array.npy)")

os.remove(np_array_filename)

## == SAVE MULTIPLE NUMPY ARRAYS INCORRECTLY =====
# -- note the file extension .npy
np_arrays_filename = "np_arrays.npz"

arr3 = arr2+100
np.savez(np_arrays_filename,arr1,arr2,arr3)
del arr1, arr2, arr3
np.load(np_arrays_filename)

if 'arr1' in globals():
    print(f"arr1 is {arr1}")
else:
    print("arr1 does not exist after np.load(np_array.npy)")

#np.savez(np_arrays_filename,arr1 = arr1,arr2 = arr2,arr3 = arr3)
np_arrays_semi_dict_obj = np.load(np_arrays_filename)
try:
    arr1 = np_arrays_semi_dict_obj["arr1"]
    print(f"arr1 is {arr1}")
except:
    print("arr1 does not exist after \n np_arrays_semi_dict_obj = np.load(np_arrays.npz) \n arr1 = np_arrays_semi_dict_obj[''arr1''] ")

## == SAVE MULTIPLE NUMPY ARRAYS CORRECTLY =====
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

arr3 = arr2+100

del np_arrays_semi_dict_obj
np.savez(np_arrays_filename,arr1 = arr1, arr2 = arr2, arr3 = arr3)

del arr1, arr2, arr3
np_arrays_semi_dict_obj = np.load(np_arrays_filename)

try:
    arr1 = np_arrays_semi_dict_obj["arr1"]
    print(f"arr1 is {arr1}")
except:
    print("arr1 does not exist after \n np_arrays_semi_dict_obj = np.load(np_arrays.npz) \n arr1 = np_arrays_semi_dict_obj[''arr1''] ")

try:
    arr2 = np_arrays_semi_dict_obj["arr2"]
    print(f"arr2 is {arr2}")
except:
    print("arr2 does not exist after \n np_arrays_semi_dict_obj = np.load(np_arrays.npz) \n arr2 = np_arrays_semi_dict_obj[''arr2'' ")

os.remove(np_arrays_filename)