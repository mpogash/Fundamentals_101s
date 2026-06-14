"""
M. Pogash 2026-06-13

pandas 101
"""


# == IMPORT LIBRARIES ====================
import numpy as np
import pandas as pd
from print_series_stats import print_series_stats

# == ARRAY CREATION ====================
lab1 = ["a","b","c","d","e","f","g","h","i"]
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# == SERIES OPERATIONS ==================
pd_series = pd.Series(arr1)
print(f"pd_series is \n {pd_series}")
print_series_stats(pd_series,"pd_series")

pd_series = pd.Series(arr1,index=lab1)
print(f"pd_series is \n{pd_series}")
print_series_stats(pd_series,"pd_series")
