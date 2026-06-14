"""
M. Pogash 2026-06-13

pandas 101
"""


# == IMPORT LIBRARIES ====================
import numpy as np
import pandas as pd
from print_series_stats import print_series_stats

# == NP ARRAY ====================
lab1 = ["a","b","c","d","e","f","g","h","i"]
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

pd_series = pd.Series(arr1)
label_str = "numpy array"
print(f"{label_str} is \n{pd_series}\n")
print_series_stats(pd_series,label_str)

pd_series = pd.Series(arr1,index=lab1)
label_str = "numpy array labeled"
print(f"{label_str} is \n{pd_series}\n")
print_series_stats(pd_series,label_str)

# == DICTIONARIES ====================
dict1 = {"Year": "2020", "Production": 0, "Morale": 75, "Phase": "Innovate"}
pd_series = pd.Series(dict1)
label_str = "dictionary"
print(f"{label_str} is \n{pd_series}\n")
print_series_stats(pd_series,label_str)

# == LIST OF DICTIONARIES ==================
dict1 = {"Year": "2020", "Production": 0, "Morale": 75, "Phase": "Innovate"}
dict2 = {"Year": "2021", "Production": 3, "Morale": 90, "Phase": "Transform"}
dict3 = {"Year": "2022", "Production": 90, "Morale": 35, "Phase": "Execute"}
dict4 = {"Year": "2023", "Production": 65, "Morale": -10, "Phase": "Cut"}

list_of_dicts = [dict1, dict2, dict3, dict4]
label_str = "list of dictionaries"
pd_series = pd.Series(list_of_dicts)
print(f"{label_str} is \n{pd_series}\n")
print_series_stats(pd_series,label_str)

# == SCALAR BROADCASTED + INDICES ==================
scalar_val = None
lab1 = ["a","b","c","d","e","f","g","h","i"]

list_of_dicts = [dict1, dict2, dict3, dict4]
label_str = "Broadcasted Scalar"
pd_series = pd.Series(scalar_val,index=lab1)
print(f"{label_str} is \n{pd_series}\n")
print_series_stats(pd_series,label_str)