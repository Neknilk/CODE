import pandas as pd
import matplotlib.pyplot as plt

# File path
file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_filled.csv'

# Load the CSV file into a DataFrame without low memory usage
df = pd.read_csv(file_path, low_memory=False)

# Convert the epoch time to datetime
df['epoch_time'] = pd.to_datetime(df['epoch_time'], unit='s')

# Filter data for flights with the number 2
df_flight_2 = df[df['flight'] == 2].copy()

# Initialize the flightphases column with 'climb'
df_flight_2['flightphases'] = 'climb'

# Find the index where altitude stops increasing for 15 minutes
climb_end_index = df_flight_2[df_flight_2['altitude'].diff().le(0)].index.min()

# Assign 'cruise' for the interval where maximum altitude is reached + 3000 buffer
max_altitude = df_flight_2['altitude'].max()
cruise_start_index = df_flight_2[df_flight_2['altitude'] >= max_altitude * 0.9].index.min()
cruise_end_index = df_flight_2[df_flight_2['altitude'] >= max_altitude].index.max()
df_flight_2.loc[cruise_start_index:cruise_end_index, 'flightphases'] = 'cruise'

# Assign 'descent' for the interval after cruise
descent_condition = df_flight_2.index > cruise_end_index
df_flight_2.loc[descent_condition, 'flightphases'] = 'descent'

# Plot the altitude with assigned phases
plt.figure(figsize=(10, 6))
plt.plot(df_flight_2['epoch_time'], df_flight_2['altitude'], label='Altitude')
plt.scatter(df_flight_2['epoch_time'], df_flight_2['altitude'], c=df_flight_2['flightphases'].map({'climb': 'red', 'cruise': 'blue', 'descent': 'green'}), label='Flight Phases', marker='o')

# Get the timestamp for the end of the climb phase
end_climb_timestamp = df_flight_2.loc[climb_end_index, 'epoch_time']

# Add a vertical line at the end of the climb phase
plt.axvline(end_climb_timestamp, color='g', linestyle='--', label='End of Climb')

# Get the timestamp for the end of the cruise phase
end_cruise_timestamp = df_flight_2.loc[cruise_end_index, 'epoch_time']

# Add a vertical line at the end of the cruise phase
plt.axvline(end_cruise_timestamp, color='r', linestyle='--', label='End of Cruise')

plt.xlabel('Time')
plt.ylabel('Altitude')
plt.title('Altitude with Flight Phases for Flight 2')
plt.legend()
plt.show()
