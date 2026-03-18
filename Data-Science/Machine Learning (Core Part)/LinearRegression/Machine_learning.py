## Basic Linear Regression Example

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

## Sample Data 
data = { 
   "Area" : [ 1000,1500,2000,3000,2500],
   "Price": [200000,300000,400000,500000,600000]
     }

df = pd.DataFrame(data)

x = df[["Area"]]  #Input

y = df[["Price"]]  # Output

# Split Data 
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

# create Model

model = LinearRegression()

# Train Model 
model.fit(x_train,y_train)

# Predict
prediction = model.predict([[2200]])

print("Predicted Price :", prediction)

## Model Evaluation

from sklearn.metrics import r2_score 

y_pred = model.predict(x_test)

print("R2 Score : ", r2_score(y_test, y_pred))

## Practice Task 


