from joblib import load
import numpy as np

# Define independent and dependent variables
independent_variables = ['ground_speed', 'vertical_rate', 'flight_duration_seconds', 'track']
dependent_variables = ['altitude', 'latitude', 'longitude']

# Corrected file paths for model loading
model_paths = {
    'climb_altitude': r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_altitude.joblib',
    'climb_latitude': r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_latitude.joblib',
    'climb_longitude': r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_longitude.joblib',
    'cruise_altitude': r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_altitude.joblib',
    'cruise_latitude': r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_latitude.joblib',
    'cruise_longitude': r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_longitude.joblib',
    'descent_altitude': r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_altitude.joblib',
    'descent_latitude': r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_latitude.joblib',
    'descent_longitude': r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_longitude.joblib',
}

# Load the models
models = {key: load(path) for key, path in model_paths.items()}

# Example input values (replace with actual user input)
example_user_inputs = {
    'ground_speed': 500,
    'vertical_rate': 1000,
    'flight_duration_seconds': 2000,
    'track': 45,
}

# Determine the phase based on user input time
if example_user_inputs['flight_duration_seconds'] < 1600:
    # Climb phase
    phase_prefix = 'climb'
elif 1600 <= example_user_inputs['flight_duration_seconds'] < 4500:
    # Cruise phase
    phase_prefix = 'cruise'
else:
    # Descent phase
    phase_prefix = 'descent'

# Predict using the corresponding models
predictions = {
    variable: models[f'{phase_prefix}_{variable}'].predict(np.array([example_user_inputs[variable] for variable in independent_variables]).reshape(1, -1))[0]
    for variable in dependent_variables
}

# Print or use the predictions and phase as needed
print(f"Predicted Phase: {phase_prefix.capitalize()}")
print(f"Predicted Altitude: {predictions['altitude']}")
print(f"Predicted Latitude: {predictions['latitude']}")
print(f"Predicted Longitude: {predictions['longitude']}")
