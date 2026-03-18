## EDA 

import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.head()) ## First 5 rows

print(df.info()) ## Dataset info

print(df.shape) ## Shape of dataset

print(df.columns) ## Column names

print(df.describe()) ## Statistical summary

print(df.isnull().sum()) ## Missing values

print(df.dropna()) ## Drop missing values

## Fill Missing Values
df.fillna(df.mean(numeric_only=True), inplace=True)

### Matplotlib

import matplotlib.pyplot as plt

df["Customer_Age"].plot(kind="hist")
plt.show()

## Bar Chart

df["Product_Category"].value_counts().plot(kind="bar")
plt.show()
