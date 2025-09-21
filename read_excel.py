import pandas as pd
import json

try:
    # Read the Excel file
    df = pd.read_excel('TOTAL AMOUNT.xlsx')
    
    # Display basic info about the dataframe
    print('=== EXCEL FILE STRUCTURE ===')
    print(f'Shape: {df.shape}')
    print(f'Original Columns: {list(df.columns)}')
    print()
    
    # Remove unnamed columns first
    df_clean = df.loc[:, ~df.columns.str.startswith('Unnamed')]
    print(f'Cleaned Columns: {list(df_clean.columns)}')
    print()
    
    print('=== FIRST FEW ROWS (CLEANED) ===')
    print(df_clean.head(10))
    print()
    
    print('=== DATA TYPES ===')
    print(df_clean.dtypes)
    print()
    
    print('=== ALL DATA (CLEANED) ===')
    print(df_clean.to_string())
    print()
    
    # Remove empty rows and fill NaN for JSON export
    df_clean = df_clean.dropna(how='all')  # Remove empty rows
    df_clean = df_clean.fillna('')   # Fill NaN with empty strings
    
    print('=== CLEANED COLUMNS ===')
    print(f'Columns after removing unnamed: {list(df_clean.columns)}')
    print()
    
    # Convert to JSON
    data_json = df_clean.to_json(orient='records', indent=2)
    
    with open('data.json', 'w') as f:
        f.write(data_json)
    
    print('=== JSON SAVED ===')
    print('Data saved to data.json (without unnamed columns)')
    print(f'Final shape: {df_clean.shape}')

except Exception as e:
    print(f'Error reading Excel file: {e}')
