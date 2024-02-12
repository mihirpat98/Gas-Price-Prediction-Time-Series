import pandas as pd

# Load the Excel file
excel_file = pd.ExcelFile('data/gas_prices_regular.xls')

# Iterate through each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(excel_file, sheet_name)
    
    # Define the output file name
    output_file = "data/"+ f'{sheet_name}.csv'
    
    # Write the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
