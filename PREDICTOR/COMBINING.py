import os
import pandas as pd

# Set the directory where your CSV files are located
directory = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\\'

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each flight number and append its data to the combined DataFrame
for i in range(1, 2634):  # Assuming flight numbers go from 1 to 2633
    file_name = f'flight{i}.csv'
    file_path = os.path.join(directory, file_name)
    
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        df['FlightNumber'] = i  # Add a new column with the flight number
        combined_data = pd.concat([combined_data, df])

# Save the combined data to a new CSV file
output_file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_file_with_flight_number.csv'
combined_data.to_csv(output_file_path, index=False)

print(f"Combined data with flight number saved to: {output_file_path}")
