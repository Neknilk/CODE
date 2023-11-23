import pandas as pd
import os

# Specify the directory where your files are located
directory_path = r'C:\Users\jayva\OneDrive\alles\Bureaublad\DATA\\'

# Iterate through files in the directory
for i in range(1, 26):
    file_name = f'File_{i}.csv'
    file_path = os.path.join(directory_path, file_name)

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the CSV file with explicit data types
        dtype_dict = {'icao24': str}  # Specify the data type of the 'icao24' column as string
        df = pd.read_csv(file_path, dtype=dtype_dict)

        # Convert the 'timestamp' column to a datetime format
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')

        # Extract date, year, month, and day into separate columns
        df['day'] = df['timestamp'].dt.day
        df['hour'] = df['timestamp'].dt.hour
        df['minute'] = df['timestamp'].dt.minute
        df['second'] = df['timestamp'].dt.second

        # Save the updated DataFrame back to the original CSV file, overwriting it
        df.to_csv(file_path, index=False)
    else:
        print(f"File '{file_path}' not found.")

print("Processing complete.")