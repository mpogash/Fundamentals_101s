import pandas as pd

def print_dataframe_stats_complete(df, df_name_str="DataFrame"):
    # print dataframe name    
    print(f"== {df_name_str} Stats =============================")

    # print dataframe sizing info
    print(f"Shape (Rows, Columns): {df.shape}")
    print(f"Total Elements:        {df.size}")
    print(f"Dimensions:            {df.ndim}")

    # print dataframe content into
    print(f"Index Type:            {type(df.index).__name__}")
    #print(f"Index Range/Length:    {len(df.index)}")
        
    # print number of nulls in each columm as a percentage
    null_counts = df.isnull().sum()
    for col in df.columns:
        dtype = df[col].dtype
        nulls = null_counts[col]
        null_pct = (nulls / len(df)) * 100
        print(f" * '{col}': dtype={dtype} | Nulls={nulls} ({null_pct:.1f}%)")
        
    # print total memory
    total_mem = df.memory_usage(deep=True).sum() / (1024 ** 2)
    print(f"Total Memory (Deep):   {total_mem:.2f} MB")
    
    # print to seprate comments above from latter text
    print("\n"*2)