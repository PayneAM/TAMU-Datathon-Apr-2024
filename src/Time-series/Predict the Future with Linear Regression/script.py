# Overview: Time series data represents values recorded a
# t consistent time intervals. This type of data analysis is
# fundamental in fields like machine learning, statistics, and
# mathematics, often starting with simple methods like linear
# regression!

# Your Challenge: You’re going to use linear regression
# (yep, the stuff from stats class) to make a prediction based on
# past data.

# Dataset: You are provided with a 'train.csv' dataset
# containing the variable "unit", which has been recorded
# annually from 2000 to 2028 (variable "date"). Your objective
# is to predict the unit value for the year 2029.

# How to Turn It In: Check out 'test_submission_example.csv'
# for how you should format your prediction. Use the data in
# 'test.csv' to make your forecast for 2029.

import pandas as pd
import csv
from sklearn import linear_model

train_df = pd.read_csv("src\\Time-series\\Predict the Future with Linear Regression\\train.csv", index_col="date",parse_dates=True)

train_df["days_from_start"] = (train_df.index - train_df.index[0]).days; train_df

x = train_df["days_from_start"].values.reshape(-1,1)
y = train_df["unit"].values

model = linear_model.LinearRegression().fit(x, y)
linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1)

test_df = pd.read_csv("src\\Time-series\\Predict the Future with Linear Regression\\test.csv", index_col="date",parse_dates=True)
test_df["days_from_start"] = (test_df.index - train_df.index[0]).days; test_df
x = test_df["days_from_start"].values.reshape(-1,1)
test_df["unit"] = list(map(round, model.predict(x)))

test_submission_df = pd.DataFrame({"\"date\"":test_df.index, "\"unit\"": test_df["unit"]})
test_submission_df.to_csv("src\\Time-series\\Predict the Future with Linear Regression\\test_submission.csv", index=False, quoting=csv.QUOTE_NONE)