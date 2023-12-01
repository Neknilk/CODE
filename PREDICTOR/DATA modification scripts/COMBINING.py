import os
import pandas as pd

# Set the directory where your CSV files are located
directory_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\\'

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each CSV file, read its data, and add the 'flight' column
for csv_file in csv_files:
    file_path = os.path.join(directory_path, csv_file)
    data = pd.read_csv(file_path)
    
    # Extract the flight number from the file name
    flight_number = int(csv_file.replace('flight', '').replace('.csv', ''))
    
    # Add the 'flight' column to the data
    data['flight'] = flight_number
    
    # Concatenate the data to the combined DataFrame
    combined_data = pd.concat([combined_data, data], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_data.to_csv(r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_data.csv', index=False)

print("CSV files combined successfully.")
