import pandas as pd
# deleted these colomns in order to make the the data file small enough to upload to brightspace so that you can use the PREDICTOR.py to get the 4D output


# Replace the file path with the actual file path of your CSV
file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_filled.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path, low_memory=False)

# List of column names to be deleted
columns_to_delete = ['Unnamed: 0', 'callsign', 'onground', 'alert', 'spi', 'last_position', 'baro_altitude', 'squawk', 'icao24' ]

# Drop the specified columns
df = df.drop(columns=columns_to_delete)

# Save the modified DataFrame back to a CSV file
df.to_csv(r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\Combined_reduced.csv', index=False)
