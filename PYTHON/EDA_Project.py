## Task 1:

import pandas as pd

df = pd.read_csv("customer_data.csv")
print(df.head()) ## First 5 rows

print(df.info()) ## Dataset info

print(df.shape) ## Shape of dataset

print(df.isnull().sum()) ## Missing values

## Fill missing values with 
print(df.fillna(df.mean(numeric_only=True), inplace=True))

## Or drop rows with missing values
print(df.dropna(inplace=True))

### Matplotlib

import matplotlib.pyplot as plt

df["label"].plot(kind="hist") ## histogram of the "label" column
plt.show()

## Bar Chart

df["label"].value_counts().plot(kind ="bar") ## bar chart of the "Number_of_houses" column
plt.show()

### Write 3 insights from data

# ---- Chart 1: Class Distribution ----
plt.figure(figsize=(6,4))
df['label'].value_counts().plot(kind='bar')
plt.title('Class Distribution (label)')
plt.xlabel('Label')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# ---- Chart 2: Positive Cases by Age Group ----
plt.figure(figsize=(6,4))
positive_by_age = df[df['label'] == 1]['Avg_age'].value_counts()
positive_by_age.plot(kind='bar')
plt.title('Positive Outcomes by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers (label = 1)')
plt.tight_layout()
plt.show()

# ---- Chart 3: Salary Distribution by Customer Main Type (Top 10) ----
plt.figure(figsize=(8,5))
top_types = df['Customer_main_type'].value_counts().head(10).index
df[df['Customer_main_type'].isin(top_types)].boxplot(column='Avg_Salary', by='Customer_main_type', rot=45)
plt.title('Salary Distribution by Customer Main Type (Top 10)')
plt.suptitle('')
plt.xlabel('Customer Main Type')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.show()