import pandas as pd

# Replace 'your_existing_data.csv' with the path to your CSV file
file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_data.csv'

# Read the existing CSV file into a DataFrame
df = pd.read_csv(file_path, low_memory=False)

# Convert 'timestamp' to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set 'timestamp' as the index
df.set_index('timestamp', inplace=True)

# Function to determine flight phase
def get_flight_phase(altitude_change):
    if altitude_change > 650:
        return 'climb'
    elif altitude_change < -2800:
        return 'descent'
    else:
        return 'cruise'

# Resample data for every 300 seconds and calculate cumulative altitude change
df_resampled = df.groupby('flight').resample('300S').agg({'altitude': 'first'}).groupby('flight').diff().fillna(method='ffill')

# Reset the index to include 'flight' and 'timestamp' columns
df_resampled.reset_index(inplace=True)

# Assign flight phase based on cumulative altitude change
df_resampled['flight_phase'] = df_resampled['altitude'].apply(get_flight_phase)

# Merge flight phase DataFrame with the original DataFrame based on 'timestamp' and 'flight'
df_combined = pd.merge(df, df_resampled[['timestamp', 'flight_phase', 'flight']], how='left', on=['timestamp', 'flight'])

# Save the combined DataFrame with flight phase as a new column
combined_output_file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_phases.csv'
df_combined.to_csv(combined_output_file_path, index=False)

# Display the result
print("finished")
