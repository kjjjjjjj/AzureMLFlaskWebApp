# For deploying Machine learning model we be concentrating on Python programming language and deployment tools for this will be Flask and Microsoft Azure. 
# We will create a web application that will run 24×7 hosted on a cloud-based server. 
# Use famous Iris flower dataset and we be storing work on Github and deploy same to Azure via Github. 

# Create an ML model
# First create a Machine learning model with name model.py and then pickling model in local system using Pickle or Joblib. 
# So how to create a easy Machine learning model of Iris flower dataset using Support Vector Machine Classification: Model.py

#import necessary libraries
from pyforest import *
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib
from sklearn.datasets import load_iris

#load dataset into a pandas dataframe
data= load_iris()
data.feature_names
df= pd.DataFrame(data.data)
df.head()

#rename columns with actual column names that is sepal and petal width and length
df.columns= data.feature_names
data.target_names

#insert target feature in dataset
df["target"]= data.target

#get our X and y to feed it into ML model
X= df.drop(["target"], axis=1)
y= df.target

#split dataset into train and test
X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=0.2, random_state=42)

#load SVC model by creating an object of class
model= SVC()

#train model
model.fit(X_train,y_train)

#making predictions
y_pred= model.predict(X_test)

#pick model
joblib.dump(model, "model.pkl")
c= [2,3,3,4]
from_jb= joblib.load("model.pkl")
from_jb.predict([c])