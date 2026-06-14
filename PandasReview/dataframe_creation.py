"""
M. Pogash 2026-06-13

pandas 101
"""

# == IMPORT LIBRARIES ====================
import numpy as np
import pandas as pd
from print_dataframe_stats import print_dataframe_stats

# == DICTIONARIES ==================
lab = ["2020","2021","2022","2023"]
dict = {
    "Production":    [0,  3, 90,  65],
    "Morale":        [75, 90, 30, -10],
    "Phase":  [ "Innovate", "Transform", "Execute", "Cut"]
}

pd_dataframe = pd.DataFrame(dict)
label_str = "dictionary"
print(f"{label_str} is \n{pd_dataframe}\n")
print_dataframe_stats(pd_dataframe,label_str)

pd_dataframe = pd.DataFrame(dict,index=lab)
label_str = "dictionary labeled"
print(f"{label_str} is \n{pd_dataframe}\n")
print_dataframe_stats(pd_dataframe,label_str)

# == NP ARRAYS ====================
lab = [["x0","x1","x2"],["y0","y1","y2"]]
np_arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

pd_dataframe = pd.DataFrame(np_arr)
label_str = "numpy array"
print(f"{label_str} is \n{pd_dataframe}\n")
print_dataframe_stats(pd_dataframe,label_str)

pd_dataframe = pd.DataFrame(np_arr,index=lab[0],columns=lab[1])
label_str = "numpy array labeled"
print(f"{label_str} is \n{pd_dataframe}\n")
print_dataframe_stats(pd_dataframe,label_str)

# == LISTS ====================
lab = [["x0","x1","x2"],["y0","y1","y2"]]
list = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

pd_dataframe = pd.DataFrame(list)
label_str = "list"
print(f"{label_str} is \n{pd_dataframe}\n")
print_dataframe_stats(pd_dataframe,label_str)

pd_dataframe = pd.DataFrame(list,index=lab[0],columns=lab[1])
label_str = "list labeled"
print(f"{label_str} is \n{pd_dataframe}\n")
print_dataframe_stats(pd_dataframe,label_str)

# == LIST OF DICTIONARIES ==================
dict1 = {"Year": "2020", "Production": 0, "Morale": 75, "Phase": "Innovate"}
dict2 = {"Year": "2021", "Production": 3, "Morale": 90, "Phase": "Transform"}
dict3 = {"Year": "2022", "Production": 90, "Morale": 35, "Phase": "Execute"}
dict4 = {"Year": "2023", "Production": 65, "Morale": -10, "Phase": "Cut"}

list_of_dicts = [dict1, dict2, dict3, dict4]
label_str = "list of dictionaries"
pd_dataframe = pd.DataFrame(list_of_dicts)
print(f"{label_str} is \n{pd_dataframe}\n")
print_dataframe_stats(pd_dataframe,label_str)
