import numpy as np

# - Print Array & Stats
def print_np_array_stats(np_array,np_array_name_str):
    print(f"{np_array_name_str} is\n {np_array}")
    print(f"{np_array_name_str}.shape is {np_array.shape}")
    print(f"{np_array_name_str}.size is {np_array.size}")
    print(f"{np_array_name_str}.ndim is {np_array.ndim}")
    print(f"{np_array_name_str}.dtype is {np_array.dtype}")
    print(f"\n")
    return
