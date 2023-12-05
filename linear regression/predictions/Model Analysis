import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.feature_selection import f_regression
from scipy.stats import f

# Load the models
models = {
    'climb': {
        'altitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_altitude.joblib'),
        'latitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_latitude.joblib'),
        'longitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\climb_linear_regression_model_longitude.joblib')
    },
    'cruise': {
        'altitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_altitude.joblib'),
        'latitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_latitude.joblib'),
        'longitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\cruise_linear_regression_model_longitude.joblib')
    },
    'descent': {
        'altitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_altitude.joblib'),
        'latitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_latitude.joblib'),
        'longitude': joblib.load(r'C:\Users\jayva\Documents\GitHub\FOE\descent_linear_regression_model_longitude.joblib')
    }
}

# Load your CSV file into a DataFrame
file_path = 'C:/Users/jayva/Documents/GitHub/FOE/DATA/FILTERED/combined_filled.csv'
df = pd.read_csv(file_path, low_memory=False)

# Define independent and dependent variables
independent_variables = ['ground_speed', 'vertical_rate', 'flight_duration_seconds', 'track']
dependent_variables = ['altitude', 'latitude', 'longitude']

# Encode the flight_phase column to numerical values
df['flight_phase_encoded'] = df['flight_phase'].astype('category').cat.codes

# Filter data for climb, descent, and cruise
climb_data = df[df['flight_phase'] == 'climb']
descent_data = df[df['flight_phase'] == 'descent']
cruise_data = df[df['flight_phase'] == 'cruise']

# Initialize lists to store overall predictions and true values
results_list = []

# Iterate over unique flight phases
for phase, phase_data in zip(['climb', 'cruise', 'descent'], [climb_data, cruise_data, descent_data]):
    # Extract features and target variables
    X = phase_data[independent_variables]
    
    for output_var, model in models[phase].items():
        y = phase_data[output_var]
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Step 1: Combine Predictions
        combined_predictions = model.predict(X_test)

        # Step 2: Combine Actual Values
        combined_actual_values = y_test

        # Step 3: Calculate R-squared
        r_squared = r2_score(combined_actual_values, combined_predictions)

        # Step 4: Calculate MSE
        mse = mean_squared_error(combined_actual_values, combined_predictions)

        # Step 5: Calculate F-statistic
        num_obs = len(y_test)
        num_predictors = 1  # Assuming one model corresponds to one predictor

        # Calculate the F-statistic
        f_statistic = (r_squared / num_predictors) / ((1 - r_squared) / (num_obs - num_predictors - 1))

        # Calculate p-value using f_regression
        f_values, p_values = f_regression(X_test, y_test, center=True)

        # Append results to the list
        results_list.append({
            'Phase': phase,
            'Output Variable': output_var,
            'R-squared': r_squared,
            'MSE': mse,
            'F-statistic': f_statistic,
            'P-value for F-statistic': p_values[0]
        })
