"""
M. Pogash 2026-06-14

pandas 101
"""


# == IMPORT LIBRARIES ====================
import numpy as np
import pandas as pd
from print_dataframe_stats import print_dataframe_stats

# == BASE DATAFRAME 2 ====================
lab = ["Metric1","Metric2","Metric3","Metric4","Metric5","Metric6"]
pd_df_2 = pd.DataFrame(np.arange(-15,15,1).reshape(5,6),columns=lab)
label_str = "Original DataFrame 2"
print(f"{label_str} is \n{pd_df_2}\n")

# column name indexing 
pd_df_2_indexed = pd_df_2[["Metric2","Metric3","Metric6"]]
label_str = 'pd_df_2_indexed = pd_df_2[["Metric2","Metric3","Metric6"]]'
print(f"{label_str} is \n{pd_df_2_indexed}\n")

# boolean indexing 
pd_df_2_indexed = pd_df_2[pd_df_2["Metric1"]>-3]
label_str = 'pd_df_2_indexed = pd_df_2[pd_df_2["Metric1"]>-3]'
print(f"{label_str} is \n{pd_df_2_indexed}\n")

# boolean indexing by specific column
pd_df_2_indexed = pd_df_2[pd_df_2["Metric1"]>-3]
label_str = 'pd_df_2_indexed = pd_df_2[pd_df_2["Metric1"]>-3]'
print(f"{label_str} is \n{pd_df_2_indexed}\n")

# boolean indexing by a filter applied to cols 
# -- breaks due to dimension mismatching with the combination 
# -- of any and axis=0 
#pd_df_2_indexed = pd_df_2[(pd_df_2>-3).any(axis=0)]
#label_str = 'pd_df_2_indexed = pd_df_2[(pd_df_2>-3).any(axis=0)]'
#print(f"{label_str} is \n{pd_df_2_indexed}\n")

# boolean indexing by a filter applied to rows
pd_df_2_indexed = pd_df_2[(pd_df_2>-3).any(axis=1)]
label_str = 'pd_df_2_indexed = pd_df_2[(pd_df_2>-3).any(axis=1)]'
print(f"{label_str} is \n{pd_df_2_indexed}\n")

# by row and col name
pd_df_2_indexed = pd_df_2.loc[3,"Metric1"]
label_str = 'pd_df_2_indexed = pd_df_2.loc[3,:"Metric1"]'
print(f"{label_str} is \n{pd_df_2_indexed}\n")

# by row and columnb index
pd_df_2_indexed = pd_df_2.iloc[3,0]
label_str = 'pd_df_2_indexed = pd_df_2.iloc[3,0]'
print(f"{label_str} is \n{pd_df_2_indexed}\n")
