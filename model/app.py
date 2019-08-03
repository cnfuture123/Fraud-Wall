from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import numpy as np

def parseData(data):
    step = data['step']
    type = data['type']
    amount = data['amount']
    oldbalanceOrg = data['oldbalanceOrg']
    newbalanceOrig = data['newbalanceOrig']
    oldbalanceDest = data['oldbalanceDest']
    newbalanceDest = data['newbalanceDest']
    isFlaggedFraud = data['isFlaggedFraud']

    return np.array([[step, type, amount, oldbalanceOrg, newbalanceOrig,
                      oldbalanceDest, newbalanceDest, isFlaggedFraud]])


app = Flask(__name__)

@app.route('/app',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print(data)
    input = parseData(data)
    prec = model.predict(input)
    result = {'isFraudFlag': str(prec[0])}

    return jsonify(result)

if __name__ == '__main__':

    model = joblib.load('../model/model.pkl')
    print("Model loaded!")
    app.run(debug=True)


