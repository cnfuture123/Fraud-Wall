# Fraud Wall
Fraud Detector With Machine Learning

## Introduction
This project is to design a fraud detector named as Fraud Wall. During online transaction processing by Payment Switch, it needs to pass a few validations for security purpose. And Fraud Wall is part of it used to detect fraud online transactions based on transaction information. Usually Fraud Wall service can be accessed through HTTP/HTTPS call with necessary transaction information as HTTP request parameters.

## Data Source
The data set is available at Kaggle - https://www.kaggle.com/ntnu-testimon/paysim1.
Actually the dataset is a synthetic dataset generated using the simulator called PaySim. PaySim simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country.
In the dataset, it contains 11 columns: step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest, newbalanceDest, isFlaggedFraud, isFraud. Please refer detail data description available at Kaggle.

## Components
![Components](image/Components.PNG)

## Run Fraud Wall Service
1.Go to "model" Folder: `$ cd model/`

2.Build Model: `$ python model.py`

3.Start Flask Application: `$ python app.py`

4.Perform HTTP Call to Flask Application Using Postman:

  - Sample HTTP Request Format:
    ```
    {
      "step": 181,
      "type": 1,
      "amount": 410299.86,
      "oldbalanceOrg": 410299.86,
      "newbalanceOrig": 0,
      "oldbalanceDest": 0,
      "newbalanceDest": 0,
      "isFlaggedFraud": 0
    }
    ```
    
  - Sample HTTP Response Format:
    ```
    {
      "isFraudFlag": "1"
    }
    
    Note: "isFraudFlag" parameter is used to indicate whether the transaction is fraud or not. 
          1 - Fraud, 0 - Not Fraud
    ```
