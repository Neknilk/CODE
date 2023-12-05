from joblib import load
import numpy as np
import pandas as pd

# Define independent and dependent variables
independent_variables = ['ground_speed', 'vertical_rate', 'flight_duration_seconds', 'track']
dependent_variables = ['altitude', 'latitude', 'longitude']

# Corrected file paths for model loading
model_paths = {
    'climb': {
        'altitude': r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_altitude.joblib',
        'latitude': r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_latitude.joblib',
        'longitude': r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_longitude.joblib',
    },
    'cruise': {
        'altitude': r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_altitude.joblib',
        'latitude': r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_latitude.joblib',
        'longitude': r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_longitude.joblib',
    },
    'descent': {
        'altitude': r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_altitude.joblib',
        'latitude': r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_latitude.joblib',
        'longitude': r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_longitude.joblib',
    },
}

# Load the models
models = {phase: {var: load(path) for var, path in paths.items()} for phase, paths in model_paths.items()}

# Get user input for the time in minutes
user_input_time_minutes = float(input("Enter the current time in minutes after takeoff: "))
user_input_time_seconds = user_input_time_minutes * 60  # Convert minutes to seconds
print('loading this may take some time.....')

# Read data from the CSV file
data = pd.read_csv(r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_reduced.csv', low_memory=False)

# Calculate the average values at the specified time
filtered_data = data[data['flight_duration_seconds'] == user_input_time_seconds]
average_inputs = {var: filtered_data[var].mean() for var in independent_variables}
average_inputs['flight_duration_seconds'] = user_input_time_seconds

# Determine the most common flight phase based on the data
most_common_flight_phase = data['flight_phase'].mode()[0]

# Use the models corresponding to the most common phase for predictions
predictions = {
    var: models[most_common_flight_phase][var].predict(np.array([average_inputs[var] for var in independent_variables]).reshape(1, -1)).item()
    for var in dependent_variables
}

# Print the average values and predictions
print(f"Most Common Phase: {most_common_flight_phase.capitalize()}")
print("Average Values:")
for var, value in average_inputs.items():
    print(f"{var}: {value}")

# Add 600 seconds (10 minutes) to the user input time
user_input_time_seconds += 600

# Update flight duration in the average inputs
average_inputs['flight_duration_seconds'] = user_input_time_seconds

# Use the models corresponding to the most common phase for predictions after 10 minutes
predictions_10m = {
    var: models[most_common_flight_phase][var].predict(np.array([average_inputs[var] for var in independent_variables]).reshape(1, -1)).item()
    for var in dependent_variables
}

# Convert the output time from seconds to minutes
output_time_minutes = user_input_time_seconds / 60

print(f"\nPredictions at {output_time_minutes} minutes:")
print(f"Predicted Altitude: {predictions_10m['altitude']}")
print(f"Predicted Latitude: {predictions_10m['latitude']}")
print(f"Predicted Longitude: {predictions_10m['longitude']}")
