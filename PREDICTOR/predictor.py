from joblib import load

# Corrected file paths for model loading
climb_altitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_altitude.joblib'
climb_latitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_latitude.joblib'
climb_longitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_longitude.joblib'

cruise_altitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_altitude.joblib'
cruise_latitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_latitude.joblib'
cruise_longitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_longitude.joblib'

descent_altitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_altitude.joblib'
descent_latitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_latitude.joblib'
descent_longitude_model_path = r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_longitude.joblib'

# Load the models
climb_altitude_model = load(climb_altitude_model_path)
climb_latitude_model = load(climb_latitude_model_path)
climb_longitude_model = load(climb_longitude_model_path)

cruise_altitude_model = load(cruise_altitude_model_path)
cruise_latitude_model = load(cruise_latitude_model_path)
cruise_longitude_model = load(cruise_longitude_model_path)

descent_altitude_model = load(descent_altitude_model_path)
descent_latitude_model = load(descent_latitude_model_path)
descent_longitude_model = load(descent_longitude_model_path)

# Take user input for independent variables
ground_speed = float(input("Enter ground speed: "))
vertical_rate = float(input("Enter vertical rate: "))
track = float(input("Enter track: "))

# Example values for independent variables (you need to replace these with actual data)
independent_values = {
    'ground_speed': ground_speed,
    'vertical_rate': vertical_rate,
    'track': track
}

# Take user input for flight duration
user_input_time = float(input("Enter the flight duration in seconds: "))

# Determine the phase based on user input time
if user_input_time < 1600:
    # Climb phase
    altitude_prediction = climb_altitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    latitude_prediction = climb_latitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    longitude_prediction = climb_longitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    phase = "Climb"
elif 1600 <= user_input_time < 4500:
    # Cruise phase
    altitude_prediction = cruise_altitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    latitude_prediction = cruise_latitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    longitude_prediction = cruise_longitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    phase = "Cruise"
else:
    # Descent phase
    altitude_prediction = descent_altitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    latitude_prediction = descent_latitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    longitude_prediction = descent_longitude_model.predict([list(independent_values.values()) + [user_input_time]])[0]
    phase = "Descent"

# Print or use the predictions and phase as needed
print(f"Predicted Phase: {phase}")
print(f"Predicted Altitude: {altitude_prediction}")
print(f"Predicted Latitude: {latitude_prediction}")
print(f"Predicted Longitude: {longitude_prediction}")
