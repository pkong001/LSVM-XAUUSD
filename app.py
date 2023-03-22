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

# Create a route api for website
@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = svm_model.predict(final_input)[0]
    # return prediction_text ( place holder )
    return render_template("home.html",prediction_text = "The prediction is {}   >>> 1 = LongTrade | 0 = No Trade".format(output))

if __name__=="__main__":
    app.run(debug=True)