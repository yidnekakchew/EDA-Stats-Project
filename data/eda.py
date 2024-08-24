import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset:
df = pd.read_csv('benin-malanville.csv')

#Load the dataset:

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

#Perform Univariate Analysis:
for col in df.columns:
    plt.figure(figsize=(10, 6))
    df[col].hist()
    plt.title(f'Histogram of {col}')
    plt.show()

print(df.describe())

#Perform Bivariate Analysis:

plt.figure(figsize=(10, 6))
sns.scatterplot(x='feature1', y='feature2', data=df)
plt.title('Scatter Plot of Feature1 vs Feature2')
plt.show()

print(df.corr())

#Perform Feature Engineering:

df['new_feature'] = df['feature1'] + df['feature2']