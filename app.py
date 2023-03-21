import pickle
from flask import Flask, request, app, jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

## Load the model
svm_model = pickle.load(open('lsvm_xauusd.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))

## create app '/' is to go to home page
## once hitting the flask app is just going to redirect to the home.html
@app.route('/')
def home():
    return render_template('home.html')

#E Create an api
@app.route('/predict_api', methods = ['POST'])
## give input in json format which captured from 'data' key, and store in data variable.
def predict_api():
    data = request.json['data']
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = svm_model.predict(new_data)
    output = int(output[0])
    return jsonify(output)

if __name__=="__main__":
    app.run(debug=True)