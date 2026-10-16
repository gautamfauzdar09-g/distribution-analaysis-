import pandas as pd
import matplotlib.pyplot as plt

# Create a numerical dataset
data = {
    'Marks': [
        35, 40, 45, 50, 52, 55, 58, 60, 62, 65,
        65, 68, 70, 72, 75, 75, 78, 80, 82, 85,
        88, 90, 92, 95, 98
    ]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Dataset:")
print(df)

# Calculate basic statistics
print("\nStatistical Summary:")
print(df['Marks'].describe())

# Create a histogram
plt.figure(figsize=(8, 5))
plt.hist(df['Marks'], bins=6, edgecolor='black')

plt.title('Distribution Analysis of Students Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)

plt.show()

# Observations
print("\nObservations:")
print("1. Marks range from 35 to 98.")
print("2. Most students scored between 60 and 85.")
print("3. The dataset shows variation in students' marks.")