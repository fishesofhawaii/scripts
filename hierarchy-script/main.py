from datetime import datetime
import pandas as pd
import math

start_time = datetime.now()

def can_connect(): 
    return True

def main(): 
    # Data
    df = pd.read_csv('input.csv')
    
    # Syntax
    header_list = list(df)
    row_count = len(df)

    print(df)
    

main()

print()
print("Duration:", datetime.now() - start_time)