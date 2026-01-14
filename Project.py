import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a small sample of weather data
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Temperature': [22, 25, 19, 21, 24],
    'Humidity': [40, 45, 50, 42, 38]
}

# 2. Load the data into a Pandas DataFrame
df = pd.DataFrame(data)

# 3. Convert 'Date' to a format Python understands
df['Date'] = pd.to_datetime(df['Date'])

# 4. Calculate the average temperature
avg_temp = df['Temperature'].mean()
print(f"The average temperature for the week is: {avg_temp}°C")

# 5. Create a Line Graph to see the pattern
plt.figure(figsize=(8, 4)) # Set the size of the graph
plt.plot(df['Date'], df['Temperature'], marker='o', color='orange', label='Temperature')

# Add labels and title
plt.title('Temperature Changes Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Show the graph
plt.show()