import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv('houses.csv')

# Create a new index starting from 1143
new_index = pd.RangeIndex(start=1144, stop=1144+len(df))

# Set the new index
df.index = new_index

# Save the DataFrame to a new CSV file
df.to_csv('predictions_with_index.csv', index=True)