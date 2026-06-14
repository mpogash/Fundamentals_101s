import pandas as pd
#import numpy as np

def print_series_stats_complete(series, series_name_str="Series"):
    # print series name   
    print(f"== {series_name_str} Stats =================")

    # print series sizing info 
    print(f"Series Name:        {series.name}")
    print(f"Data Type (dtype):  {series.dtype}")
    print(f"Length (Size):      {len(series)}")
    print(f"Dimensions:         {series.ndim}  # (Always 1 for a Series)")
    
    # print series index info
    print(f"Index Type:         {type(series.index).__name__}")
    #print(f"Index Length:       {len(series.index)}")
    
    # print null count as a percent
    null_count = series.isnull().sum()
    null_pct = (null_count / len(series)) * 100
    print(f"Null Count:         {null_count} ({null_pct:.1f}%)")
    
    # print min mean max
    if series.dropna().empty:
        print("Series is empty or entirely null.")
    elif pd.api.types.is_numeric_dtype(series):
        # Numeric breakdown
        print(f"Min value:          {series.min()}")
        print(f"Max value:          {series.max()}")
        print(f"Mean (Average):     {series.mean():.4f}")
        print(f"Median (50th %):    {series.median():.4f}")
    else:
        # Categorical/Object breakdown
        print(f"Unique Values:      {series.nunique()}")
        top_val = series.mode().iloc[0] if not series.mode().empty else "N/A"
        print(f"Most Frequent:      '{top_val}' (Count: {series.value_counts().iloc[0]})")
        
    # print memory usage
    total_mem = series.memory_usage(deep=True) / (1024 ** 2)
    print(f"Memory (Deep):      {total_mem:.4f} MB")

    # print to seprate comments above from latter text
    print("\n"*2)
