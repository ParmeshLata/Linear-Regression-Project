import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


## CREATING DATAFRAME
df=pd.read_csv("weight-height.csv")
x_true=df[["WEIGHT"]]
y_true=df["HEIGHT"]


## SEPERATING TEST DATA AND TRAIN DATA
x_train, x_test, y_train, y_test=train_test_split(x_true, y_true, test_size=0.25, random_state=42)


## STANDARDIZATION
standard_scaler=StandardScaler()
x_train=standard_scaler.fit_transform(x_train)
x_test=standard_scaler.transform(x_test)


## MODEL GENERATING
model=LinearRegression()
model.fit(x_train, y_train)
#print(f"Coefficient : {model.coef_}")
#print(f"Intercept : {model.intercept_}")


## VALUE PREDICTION FROM TRAIN DATA
y_train_predict=model.predict(x_train)


## TEST DATA PREDCTION
y_test_pred=model.predict(x_test)


## PLOTTING THE BEST FIT LINE
best_fit_line=plt.plot(x_train, y_train_predict)
plt.xlabel("WEIGHT (TRAINED)")
plt.ylabel("HEIGHT (PREICTED)")
true_value_graph=plt.scatter(x_train, y_train)
plt.xlabel("WEIGHT (in kg)")
plt.ylabel("HEIGHT (in cm)")


## ACCURACY OF MODEL
accuracy_score=r2_score(y_test, y_test_pred)
#print(f"R square value is : {accuracy_score}")


## MODEL FOR ANY RANDOM VALUE PREDICTION
output=model.predict(standard_scaler.transform([[80]]))
print(output)