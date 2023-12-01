import pandas as pd

# Read the CSV file into a DataFrame
file_path = r'C:\Users\jayva\Documents\GitHub\FOE\DATA\FILTERED\combined_data.csv'
df = pd.read_csv(file_path, low_memory=False)

# Convert the 'epoch_time' column to epoch time and create a new 'epoch_time' column
df['epoch_time'] = (pd.to_datetime(df['epoch_time'], format='%Y-%m-%d %H:%M:%S')
                    .astype('int64') // 10**9)

# Save the updated DataFrame to the original CSV file, overwriting it
df.to_csv(file_path, index=False)
