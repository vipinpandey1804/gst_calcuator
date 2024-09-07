import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_excel('C:\\Users\\v9808\\Downloads\\test.xlsx', sheet_name='B2B')
df = df.drop([0,1,2,3,4])
df = df.infer_objects(copy=False)
filters = [0, 0.25, 1.50, 3, 5, 12, 18, 28]
total_taxable_value = 0
total_igst_value = 0
total_cgst_value = 0
total_sgst_value = 0
for rate in filters:
    filtered_df = df[df['Unnamed: 8'] == rate]
    taxable_value = filtered_df['Unnamed: 9'].sum()
    igst_value = filtered_df['Unnamed: 10'].sum()
    cgst_value = filtered_df['Unnamed: 11'].sum()
    sgst_value = filtered_df['Unnamed: 12'].sum()
    
    # Add to cumulative totals
    total_taxable_value += taxable_value
    total_igst_value += igst_value
    total_cgst_value += cgst_value
    total_sgst_value += sgst_value
    
    # Print the sums for the current filter
    print(f"Rate: {rate}%")
    print(f"Taxable Value: {taxable_value}")
    print(f"IGST: {igst_value}")
    print(f"CGST: {cgst_value}")
    print(f"SGST: {sgst_value}")
    print("-" * 40)

# Print total for all rates
print("Total for all rates:")
print(f"Total Taxable Value: {total_taxable_value}")
print(f"Total IGST: {total_igst_value}")
print(f"Total CGST: {total_cgst_value}")
print(f"Total SGST: {total_sgst_value}")