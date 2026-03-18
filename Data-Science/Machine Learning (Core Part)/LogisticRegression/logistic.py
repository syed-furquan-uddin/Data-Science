## Import Libraries 

from pyexpat import model

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

## create dataset
 
data ={
    "Study_Hours": [1,2,3,4,5,6,7,8],
    "Pass": [0,0,0,0,1,1,1,1]  
}

df = pd.DataFrame(data)

print(df)

x= df[["Study_Hours"]]
y= df[["Pass"]]

## Train Model
x_train,x_test , y_train , y_test = train_test_split(x ,y , test_size=0.2)
model = LogisticRegression()
model.fit(x_train, y_train)

## Predict

prediction = model.predict([[5]])
print("Prediction:", prediction)

## Model Evaluation (Very Important for Interviews)
## 1️⃣ Accuracy

y_pred = model.predict(x_test)
print("Accuracy :" , accuracy_score(y_test,y_pred))

## Confusion Matrix
print(confusion_matrix(y_test, y_pred))

## Precision, Recall, F1 Score
from sklearn.metrics import classification_report
print((classification_report(y_test,y_pred)))