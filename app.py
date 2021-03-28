# Creating Flask App After creating model.py file and pickling same next step is create a Flask web app with name app.py and to create this we must follow below-mentioned steps. 
# model.py, model.pkl, app.py should be present in same directory of computer. 
# reason for selecting Flask is it is a light web framework that helps in creating web apps with minimal lines of code. 
# though many frameworks for Python for creating web apps like Django, Web2py, Grok, TurboGears, etc, still Flask helps us in creating apps with less involvement of time and is a good tool for beginners who want to learn building web applications. 
# framework depends completely on Python for coding related stuff instead of relying on other dependent tools. 
# To learn insights of this amazing library one must good knowledge related to Python, a bit of HTML and CSS, a Database management system if any data-related work is involved. 
# So, if you have knowledge of these three things then you are ready to code in Flask.

#import necessary libraries for deployment
from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib
# import joblib
from pyforest import *

#naming our app as app
app= Flask(__name__)
#load pickle file for creating web app
model= joblib.load(open("model.pkl", "rb"))

#define different pages of html and specifying features required to be filled in html form
@app.route("/")
def home():
    return render_template("index.html")
    #creating a function for prediction model by specifying parameters and feeding it to ML model

@app.route("/predict", methods=["POST"])
def predict():
    #specifying our parameters as data type float
    int_features= [float(x) for x in request.form.values()]
    final_features= [np.array(int_features)]
    prediction= model.predict(final_features)
    output= round(prediction[0], 2)
    return render_template("index.html", prediction_text= "flower is {}".format(output))

#running flask app
if __name__ == "__main__":
    app.run(debug=True)