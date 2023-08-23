import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.common import random_state
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

files  = pd.read_csv('temps.csv')
# Columns: year, month, day, day of the week, Max temp for 2 days ago, Max temp for one day ago, ...
files.head(5)
print('Checking data dimentions:',files.shape)

# Quick summary statistic
files.describe()
plt.plot(files['month'],files['average'])

# One_Hot encoding
files = pd.get_dummies(files)
files.iloc[:,5:].head(5)

# Features and target
labels = np.array(files['actual'])   # Labels that we wanna predict
files = files.drop('actual', axis=1) # Removing the labels from the data
ColumnsNam = list(files.columns)     # Saving columns names
files = np.array(files)              # Converting to array

# Splitting Data to trainig and testing part
trainfeatures, testfeatures, trainlabel, testlabel = train_test_split(files, labels, test_size=0.25, random_state=42)

# Baseline Error
base_predic = testfeatures[:,ColumnsNam.index('average')]
base_Error = abs(base_predic - testlabel) 
mean_BE =round(np.mean(base_Error),2)

# Training model
rf = RandomForestRegressor(n_estimators=1000, random_state=42)
rf.fit(trainfeatures, trainlabel)

predictions = rf.predict(testfeatures)
error_model = abs(predictions - testlabel)
mean_ME = round(np.mean(error_model),2)
