## Pandas 

import pandas as pd

data = {
    "Name " : ["Furquan","ali", "abdul"],
    "Age": [20,21,34],
    "Salary ": [500000,40000,30000]
    }
df = pd.DataFrame(data)
print(df)

## First Rows

print(df.head())

## Dataset info 

print(df.info())

## Statistical Summary

print(df.describe())

## Selecting Column

print(df["Name "])

## Filtering data 
print(df[df["Age"]>23])

## Task 1:
## Create DataFrame:

data ={ "Name ":["A", "B","C"],
         "Marks ": [80,7,90],
         "City":["Delhi","Mumbai","Patna"]
        
       }
df = pd.DataFrame(data)
print(df)

print(df.head()) ## Head 
print(df.describe()) ## Statistical Summary
## Task 2:
## Filter

print(df[df["Marks "]>75]) 

## Task 3 (Mini Challenge):
## Add new column:
""""Pass"
If Marks >= 75 → Pass
Else → Fail """

df["Pass"] = df["Marks "].apply(lambda x: "Pass" if x >= 75 else "Fail")

print(df)
