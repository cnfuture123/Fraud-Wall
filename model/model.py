
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import KFold, cross_val_score, train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score
import lightgbm

#load train data
raw_data = pd.read_csv('../Dataset/train_data.csv')
print("Train data size: " + str(raw_data.shape[0]))
print("Train data columns: " + str(raw_data.columns))

from sklearn.utils import shuffle
#shuffle train data
train_data = shuffle(raw_data)
train_data = train_data.reset_index(drop=True)

#check fraud data and normal data
fraud_data = train_data[train_data['isFraud']==1]
normal_data = train_data[train_data['isFraud']!=1]
print("Fraud data size: " + str(fraud_data.shape[0]))
print("Normal data size: " + str(normal_data.shape[0]))

#Split train data and label
train_x = train_data.drop(['isFraud'], axis=1)
train_y = train_data['isFraud']

lgb = lightgbm.LGBMClassifier(n_estimators=1000,learning_rate=0.09)
model = lgb.fit(train_x, train_y)

from sklearn.externals import joblib
joblib.dump(model, '../model/model.pkl')
print("Model dumped!")


