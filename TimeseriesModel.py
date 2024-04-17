#This script performs several setps of time series analyis
# First section: Order selection for ARIMAX model based on lowest AIC and BIC for both the base case (without ex. variables)
# and with all variables
# Second section: Testing for model performance improvement when including sentiment scores
# Third section: Testing for model performance improvement when including sentiment scores and economic variables
# Fourth section: Fitting LSTM model for comparison, again with base case, including only sentiment scores, and including both sentiment scores and economic variables

# The aim of our research is not to identify multicollinearity, endogeneity, the only purpose is to test in all the following scripts whether the predictive power of two different models can be improved.

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX


df = pd.read_csv('finalDF.csv', index_col='Date', parse_dates=True)
train = df[:'2020-01-01']
test = df['2020-01-02':]

pricetrain = train["price"]
pricetest = test["price"]

exotrain = train.drop(columns=["price"])
exotest = test.drop(columns=["price"])

#First section


model = SARIMAX(pricetrain, exog=exotrain, order=(3,3,2))
results = model.fit()
print(results.summary())
