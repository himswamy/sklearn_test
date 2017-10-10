# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
import pandas as pd
import os
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler
import pickle
from sklearn.externals import joblib

from flask import Flask, abort, jsonify, request

my_auto_sklearn = pickle.load(open('auto_sklearn.pkl','rb'))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    data = request.get_json(force=True)
    predict_request = [data['msg_test']]
    predict_request = np.array[predict_request]
    y_hat = my_auto_sklearn.predict(msg_test)
    output = [y_hat[0]]
    
    return jsonify(result=output);

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]



if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
