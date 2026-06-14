"""
M. Pogash 2026-06-13

pandas 101
"""


# == IMPORT LIBRARIES ====================
import numpy as np
import pandas as pd
from print_dataframe_stats import print_dataframe_stats


# == ARRAY CREATION ====================
lab2 = [["x0","x1","x2"],["y0","y1","y2"]]
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

lab3 = ["2020","2021","2022","2023"]
dict3 = {
    "Production":    [0,  3, 90,  65],
    "Morale":        [75, 90, 30, -10],
    "Phase":  [ "Innovate", "Transform", "Execute", "Cut"]
}

# == DATAFRAME OPERATIONS ==================
pd_dataframe = pd.DataFrame(arr2)
print(f"pd_dataframe is \n{pd_dataframe}")
print_dataframe_stats(pd_dataframe,"pd_dataframe")

pd_dataframe = pd.DataFrame(arr2,index=lab2[0],columns=lab2[1])
print(f"pd_dataframe is \n{pd_dataframe}")
print_dataframe_stats(pd_dataframe,"pd_dataframe")

pd_dataframe = pd.DataFrame(dict3,index=lab3)
print(f"pd_dataframe is \n{pd_dataframe}")
print_dataframe_stats(pd_dataframe,"pd_dataframe")