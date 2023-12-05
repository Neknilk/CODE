import pandas as pd
# because of linear regression the flight needs to be seperated into 3 phases climb descent and cruise. this is the code that assigns the phases. 
# it will look at the altitude change over a period of 5 minutes. it will assign climb of that difference is > 500, descent when it is smaller then -1000. and inbetween will be cruise.
# this will analyse the change for every 300 seconds so there will be an entrie by 300 seconds after takeoff 600, 900, 1200, etc. another script will fille in the phases inbetween


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
    if altitude_change > 500:
        return 'climb'
    elif altitude_change < -1000:
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
