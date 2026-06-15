"""
M. Pogash 2026-06-13

pandas 101
"""


# == IMPORT LIBRARIES ====================
import numpy as np
import pandas as pd
from print_dataframe_stats import print_dataframe_stats

# == BASE DATAFRAME 1 ====================
pd_dataframe_1 = pd.DataFrame(np.arange(-5,5,1))
label_str = "Original DataFrame"
print(f"{label_str} is \n{pd_dataframe_1}\n")
print_dataframe_stats(pd_dataframe_1,label_str)

## == DROPPING ELEMENTS =================
# drop index incorrectly
pd_dataframe_1.drop([2])
label_str = "pd_dataframe_1.drop([2])"
print(f"{label_str} is \n{pd_dataframe_1}\n")
print_dataframe_stats(pd_dataframe_1,label_str)

# drop index corrrectly
pd_dataframe_drop = pd_dataframe_1.drop([2])
label_str = "pd_dataframe_drop = pd_dataframe_1.drop([2])"
print(f"{label_str} is \n{pd_dataframe_drop}\n")
print_dataframe_stats(pd_dataframe_drop,label_str)

# drop indices correctly 
pd_dataframe_drop = pd_dataframe_1.drop([indx_drop for indx_drop in range(2,4)])
label_str = "pd_dataframe_drop = pd_dataframe_1.drop([indx_drop for indx_drop in range(2,4)])"
print(f"{label_str} is \n{pd_dataframe_drop}\n")
print_dataframe_stats(pd_dataframe_drop,label_str)

# drop index with boolean filter
pd_dataframe_drop = pd_dataframe_1[pd_dataframe_1[0] != -1]
label_str = "pd_dataframe_drop = pd_dataframe_1[pd_dataframe_1[0] != -1]"
print(f"{label_str} is \n{pd_dataframe_drop}\n")
print_dataframe_stats(pd_dataframe_drop,label_str)

# drop indices with boolean filter
pd_dataframe_drop = pd_dataframe_1[~pd_dataframe_1[0].isin([-1, 2])]
label_str = "pd_dataframe_drop = pd_dataframe_1[~pd_dataframe_1[0].isin([-1, 2])]"
print(f"{label_str} is \n{pd_dataframe_drop}\n")
print_dataframe_stats(pd_dataframe_drop,label_str)

# drop indices in place
pd_dataframe_1_copy = pd_dataframe_1.copy()
pd_dataframe_1_copy.drop([2],inplace=True)
label_str = "pd_dataframe_1_copy = pd_dataframe_1.copy(); pd_dataframe_1_copy.drop([2],inplace=True)"
print(f"{label_str} is \n{pd_dataframe_1_copy}\n")
print_dataframe_stats(pd_dataframe_1_copy,label_str)

# drop nan elements
pd_dataframe_1_copy = pd_dataframe_1.copy()
pd_dataframe_1_copy[1, 2, 3] = None
pd_dataframe_1_copy = pd_dataframe_1_copy.dropna()
label_str = "pd_dataframe_1_copy = pd_dataframe_1_copy.dropna()"
print(f"{label_str} is \n{pd_dataframe_1_copy}\n")
print_dataframe_stats(pd_dataframe_1_copy,label_str)

# == BASE DATAFRAME 2 ====================
lab = ["Metric1","Metric2","Metric3","Metric4","Metric5","Metric6"]
pd_dataframe_2 = pd.DataFrame(np.arange(-15,15,1).reshape(5,6),columns=lab)
label_str = "Original DataFrame 2"
print(f"{label_str} is \n{pd_dataframe_2}\n")
print_dataframe_stats(pd_dataframe_2,label_str)

# Drop Columns
pd_dataframe_2_drop = pd_dataframe_2.drop(["Metric2"], axis=1)
label_str = "pd_dataframe_2_drop = pd_dataframe_2.drop(['Metric2'], axis=1)"
print(f"{label_str} is \n{pd_dataframe_2_drop}\n")
print_dataframe_stats(pd_dataframe_2_drop,label_str)