

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# Load your data
df = pd.read_csv('sierraleone-bumbuna.csv')

# Summary statistics
summary_stats = df.describe()
print(summary_stats)


# Checking for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Identifying outliers using Z-Score
from scipy import stats

z_scores = stats.zscore(df.select_dtypes(include=[float, int]))
outliers = (abs(z_scores) > 3).sum(axis=0)
print("Outliers detected:\n", outliers)



# Plotting GHI, DNI, DHI, Tamb over time
plt.figure(figsize=(15, 8))
df['GHI'].plot(label='GHI')
df['DNI'].plot(label='DNI')
df['DHI'].plot(label='DHI')
df['Tamb'].plot(label='Tamb')
plt.legend()
plt.title("Time Series Analysis")
plt.xlabel("Time")
plt.ylabel("Value")
#plt.show()

# Save the plot as a PNG file
plt.savefig("time_series_analysis.png", dpi=300)

#plt.savefig("time_series_analysis_high_quality.png", dpi=600, bbox_inches='tight')

# Display the plot
plt.show()



# Assuming 'Cleaning' column is a boolean indicator
df_cleaned = df[df['Cleaning'] == 1]

# Plotting ModA and ModB before and after cleaning
plt.figure(figsize=(15, 8))
df['ModA'].plot(label='ModA - Original')
df_cleaned['ModA'].plot(label='ModA - Cleaned')
df['ModB'].plot(label='ModB - Original')
df_cleaned['ModB'].plot(label='ModB - Cleaned')
plt.legend()
plt.title("Sensor Readings Before and After Cleaning")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
