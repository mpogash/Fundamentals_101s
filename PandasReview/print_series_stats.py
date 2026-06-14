import pandas as pd

def print_series_stats(series, series_name_str="Series"):
    # print series name   
    print(f"== {series_name_str} Stats =================")

    # print series sizing info 
    print(f"Series Name:        {series.name}")
    print(f"Data Type (dtype):  {series.dtype}")
    print(f"Length (Size):      {len(series)}")
    print(f"Dimensions:         {series.ndim}")
    
    # print null count as a percent
    null_count = series.isnull().sum()
    null_pct = (null_count / len(series)) * 100
    print(f"Null Count:         {null_count} ({null_pct:.1f}%)")
    
    # print memory usage
    total_mem = series.memory_usage(deep=True) / (1024 ** 2)
    print(f"Memory (Deep):      {total_mem:.4f} MB")

    # print to seprate comments above from latter text
    print("\n"*2)
