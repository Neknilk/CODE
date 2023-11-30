import pandas as pd

# Replace 'your_existing_data.csv' with the path to your CSV file
file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_data.csv'

# Read the existing CSV file into a DataFrame
df = pd.read_csv(file_path, low_memory=False)

# Function to determine flight phase
def get_flight_phase(altitude_change):
    if altitude_change > 750:
        return 'climb'
    elif altitude_change < -750:
        return 'descent'
    else:
        return 'cruise'

# Set 'epoch_time' as the index
df.set_index('epoch_time', inplace=True)

# Resample data for every 300 seconds and calculate cumulative altitude change
df_resampled = df.groupby('flight').resample('300S').agg({'altitude': 'first'}).groupby('flight').diff().fillna(0)

# Reset the index to include 'flight' and 'epoch_time' columns
df_resampled.reset_index(inplace=True)

# Assign flight phase based on cumulative altitude change
df_resampled['flight_phase'] = df_resampled['altitude'].apply(get_flight_phase)

# Merge flight phase DataFrame with the original DataFrame based on 'epoch_time' and 'flight'
df_combined = pd.merge(df, df_resampled[['epoch_time', 'flight_phase', 'flight']], how='left', on=['epoch_time', 'flight'])

# Save the combined DataFrame with flight phase as a new column
combined_output_file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_with_phases.csv'
df_combined.to_csv(combined_output_file_path, index=False)

# Display the result
print(df_combined[['timestamp', 'flight_phase', 'flight']])
