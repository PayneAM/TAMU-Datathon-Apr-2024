# Overview: This second challenge dives into more
# complex time series forecasting that incorporates
# trend analysis, seasonality, and autocorrelation.
# These elements are crucial for understanding
# patterns over time and making accurate predictions,
# especially in data with periodic fluctuations and
# long-term trends.

# Trend analysis identifies consistent upward or
# downward movements in data over time, helping to
# predict long-term changes. Seasonality captures
# predictable patterns that recur periodically, such as
# monthly or annually, vital for adjusting predictions
# based on expected fluctuations. Autocorrelation
# measures the relationship between current and past
# data values, highlighting the influence of historical
# data on future predictions, crucial for models that
# forecast based on previous trends.

# Your Challenge: Choose from a range of models —
# including but not limited to AR, MA, ARMA, ARIMA, and
# SARIMA — to predict future data points. This
# challenge is about applying more advanced 
# techniques to see which best captures the dynamics
# of the dataset.

# Dataset: You will use the 'train.csv' dataset, which
# includes the "unit" variable recorded monthly from
# 1950 to 1982. Your task is to forecast the value of "unit"
# for the next 12 months.

# How to Turn It In: Check out
# 'test_submission_example.csv' for how you should
# format your prediction. Use the data in 'test.csv' to
# make your forecast.

import csv
import pandas as pd 
from statsmodels.tsa.statespace.sarimax import SARIMAX 

train_df = pd.read_csv("src\\Time-series\\Time Series Mastery Challenge\\train.csv", index_col="date",parse_dates=True)
test_df = pd.read_csv("src\\Time-series\\Time Series Mastery Challenge\\test.csv", index_col="date",parse_dates=True)

model = SARIMAX(train_df["unit"], order=(1,1,1), seasonal_order=(2,1,2, 12))
result = model.fit()

predictions = result.predict(len(train_df), len(train_df)+len(test_df)-1)

predictions = pd.DataFrame({"\"date\"":predictions.index.to_list(), "\"unit\"":list(map(round, predictions.values.tolist()))})
predictions.to_csv("src\\Time-series\\Time Series Mastery Challenge\\test_submission.csv", index=False, quoting=csv.QUOTE_NONE)