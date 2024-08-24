

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib import cm


# Load your data
df = pd.read_csv('sierraleone-bumbuna.csv')

# Summary statistics
summary_stats = df.describe()
print(summary_stats)



#Data Quality Check

# Checking for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Identifying outliers using Z-Score
from scipy import stats

z_scores = stats.zscore(df.select_dtypes(include=[float, int]))
outliers = (abs(z_scores) > 3).sum(axis=0)
print("Outliers detected:\n", outliers)


# Time Series Analysis
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


#Evaluate the Impact of Cleaning

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
#plt.show()

# Save the plot as a high-quality PNG file
plt.savefig("sensor_readings_cleaning_comparison.png", dpi=300)

# Display the plot
plt.show()


#Correlation Analysis


# Correlation matrix

numeric_df = df.select_dtypes(include=[float, int])

# Calculate the correlation matrix on the numeric data
corr_matrix = numeric_df.corr()

# Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix_heatmap.png", dpi=600, bbox_inches='tight')
plt.show()





#Wind Analysis

# Assuming 'WD' is wind direction in degrees and 'WS' is wind speed
plt.figure(figsize=(10, 8))
plt.subplot(projection='polar')
plt.scatter(df['WD'] * (np.pi / 180), df['WS'], c=df['WS'], cmap=cm.viridis)
plt.title("Wind Speed and Direction")

plt.savefig("Wind Speed and Direction.png", dpi=300)
plt.show()



#Temperature Analysis

 
# Scatter plot with RH as color dimension
plt.figure(figsize=(10, 8))
plt.scatter(df['RH'], df['Tamb'], c=df['GHI'], cmap='coolwarm')
plt.colorbar(label='GHI')
plt.xlabel('Relative Humidity (RH)')
plt.ylabel('Temperature (Tamb)')
plt.title("RH vs Temperature with GHI as Color Dimension")

plt.savefig("RH vs Temperature with GHI as Color Dimension.png", dpi=300)
plt.show()




# Histograms
df[['GHI', 'DNI', 'DHI', 'WS', 'Tamb']].hist(figsize=(15, 10), bins=20)

plt.savefig("Histograms.png", dpi=300)
plt.show()


#  Z-Score Analysis
df_zscores = df.select_dtypes(include=[float, int]).apply(stats.zscore)
outliers_z = (abs(df_zscores) > 3)
print("Data points with significant deviations:\n", df[outliers_z.any(axis=1)])


# Bubble chart
plt.figure(figsize=(10, 8))
plt.scatter(df['GHI'], df['Tamb'], s=df['RH'], alpha=0.5, c=df['WS'], cmap='viridis')
plt.colorbar(label='Wind Speed (WS)')
plt.xlabel('GHI')
plt.ylabel('Temperature (Tamb)')
plt.title("GHI vs Tamb with Bubble Size as RH and Color as WS")

plt.savefig("GHI vs Tamb with Bubble Size as RH and Color as WS.png", dpi=300)
plt.show()



#Data Cleaning


# Filling missing values
df.fillna(method='ffill', inplace=True)

# Removing columns with too many null values
df.drop(columns=['Comments'], inplace=True)

# Removing outliers
df_clean = df[(abs(z_scores) < 3).all(axis=1)]



