import joblib
import matplotlib.pyplot as plt
import numpy as np

# Load the model for altitude
model_altitude = joblib.load('C:\\Users\\jayva\\Documents\\GitHub\\FOE\\climb_linear_regression_model_altitude.joblib')

# Set specific values for the other independent variables (random)
ground_speed = 438
vertical_rate = 558
flight_duration_seconds = 1200
track = 341.79

# Create a synthetic time sequence from 1 to 7000 seconds
time_sequence = np.arange(1, 7001, 1)

# Generate predictions for altitude using the specified values and constant flight duration
independent_variables_altitude = np.array([[ground_speed, vertical_rate, flight_duration_seconds, track] for _ in range(len(time_sequence))])
altitude_predictions = model_altitude.predict(independent_variables_altitude)

# Plot the regression line for altitude over time
plt.plot(time_sequence, altitude_predictions, color='red', label='Altitude Prediction')
plt.xlabel('Time (seconds)')
plt.ylabel('Altitude')
plt.title('Linear Regression Model Visualization for Altitude over Time')
plt.legend()

plt.show()
