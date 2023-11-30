import pandas as pd

# Specify the path to your dataset
file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_data.csv'

# Read the dataset into a DataFrame
df = pd.read_csv(file_path)

# Count the number of unique values in the 'flights' column
unique_values_count = df['flight'].nunique()

# Print the result
print(f'The number of unique values in the "flights" column is: {unique_values_count}')
