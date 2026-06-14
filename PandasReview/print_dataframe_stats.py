import pandas as pd
import numpy as np

def print_dataframe_stats(df, df_name_str="DataFrame"):
    # print dataframe name    
    print(f"== {df_name_str} Stats =============================")

    # print dataframe sizing info
    print(f"Shape (Rows, Columns): {df.shape}")
    print(f"Total Elements:        {df.size}")
    print(f"Dimensions:            {df.ndim}")
    total_mem = df.memory_usage(deep=True).sum() / (1024 ** 2)
    print(f"Total Memory (Deep):   {total_mem:.2f} MB")
    
    # print to seprate comments above from latter text
    print("\n"*2)