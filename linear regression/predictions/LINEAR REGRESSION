import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load your CSV file into a DataFrame
file_path = 'C:/Users/jayva/Documents/GitHub/FOE/DATA/FILTERED/combined_filled.csv'
df = pd.read_csv(file_path, low_memory=False)

# Define independent and dependent variables
independent_variables = ['ground_speed', 'vertical_rate', 'flight_duration_seconds', 'track']
dependent_variables = ['altitude', 'latitude', 'longitude']

# Filter data for climb, descent, and cruise
climb_data = df[df['flight_phase'] == 'climb']
descent_data = df[df['flight_phase'] == 'descent']
cruise_data = df[df['flight_phase'] == 'cruise']

# Encode the flight_phase column to numerical values
df['flight_phase_encoded'] = df['flight_phase'].astype('category').cat.codes

# this makes climb cruise and descent models where each output lat long and altitude will also be a seperate model
for phase, phase_data in zip(['climb', 'cruise', 'descent'], [climb_data, cruise_data, descent_data]):
    # Extract features and target variables
    X = phase_data[independent_variables]
    y = phase_data[dependent_variables]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model for each dependent variable
    for idx, dependent_variable in enumerate(dependent_variables):
        model = LinearRegression()

        # Train the model
        model.fit(X_train, y_train[dependent_variable])

        # Make predictions on the test set
        predictions = model.predict(X_test)

        # Evaluate the model performance
        mse = mean_squared_error(y_test[dependent_variable], predictions)
        r_squared = r2_score(y_test[dependent_variable], predictions)
        
        print(f"Flight Phase {phase}, Dependent Variable {dependent_variable}:")
        print(f"Mean Squared Error = {mse}")
        print(f"R-squared = {r_squared}")

        # Save the model
        model_name = f"{phase.lower()}_linear_regression_model_{dependent_variable.lower()}.joblib"
        joblib.dump(model, model_name)
