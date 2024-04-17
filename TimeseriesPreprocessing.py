import pandas as pd
import numpy as np
import os as os
import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader.data as pdr


tickers = ['AAPL', 'MSI', 'GOOGL']

price_data = yf.download(tickers, start='2012-01-01', end='2022-12-31', interval='1mo')['Close']

#we have to download the data separately for Samsung as it is not in US prices:
samsung_data = yf.download('005930.KS', start='2012-01-01', end='2022-12-31', interval='1mo')['Close']

#fetching usd/krw historical exchange rate to convert samsung KWR stock price to USD stock price
exchange_rates = pdr.DataReader('DEXKOUS', 'fred', start='2012-01-01', end='2022-12-31')
exchange_rates = exchange_rates.resample('1ME').ffill().reindex(samsung_data.index, method='nearest')
price_data['SAMS'] = samsung_data / exchange_rates['DEXKOUS']
order = ['AAPL', 'SAMS', 'GOOGL', 'MSI']
price_data = price_data[order]



weights = [0.6823, 0.2520, 0.0390, 0.0267]
weighted_prices = price_data.multiply(weights, axis='columns')
portfolio_value = weighted_prices.sum(axis=1)

#Next, we will preprocess the other exogenous variables, which includes the CPI growth rate in the US, GDP growth rate, unemployment rate, and the Michigan Sentiment Consumer Index
class PreprocessCPIGrowth:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        self.data["Date"] = pd.to_datetime(self.data["DATE"], format='%Y/%m/%d')
        self.data = self.data.sort_values("Date")
        self.data = self.data[(self.data["Date"] >= '2012-01-01') & (self.data["Date"] <= '2022-12-31')]
        self.data = self.data.groupby(self.data["Date"].dt.to_period("M")).last()
        if 'DATE' in self.data.columns:
            self.data.drop(columns=['DATE'], inplace=True)
            self.data.reset_index(drop=True, inplace=True)
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        return self.data


cpigrowth = pd.read_csv("cpigrowth.csv")
cpigrowth_preprocessed = PreprocessCPIGrowth(cpigrowth)
cpigrowth = cpigrowth_preprocessed.preprocess()

class PreprocessUnemploymentRate:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        self.data["Date"] = pd.to_datetime(self.data["DATE"], format='%Y-%m-%d')
        self.data = self.data.sort_values("Date")
        self.data = self.data[(self.data["Date"] >= '2012-01-01') & (self.data["Date"] <= '2022-12-31')]
        self.data = self.data.groupby(self.data["Date"].dt.to_period("M")).last()
        self.data.drop(columns=["DATE", "Date"], inplace=True)
        return self.data

unemploymentrate = pd.read_csv("unemploymentrate.csv")
unemploymentrat_preprocessed = PreprocessUnemploymentRate(unemploymentrate)
unemploymentrate = unemploymentrat_preprocessed.preprocess()

class PreprocessMichiganSentiment:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        self.data["Date"] = pd.to_datetime(self.data["YYYY"].astype(str) + '-' + self.data["Month"], format='%Y-%B')
        self.data = self.data.sort_values("Date")
        self.data = self.data[(self.data["Date"] >= '2012-01-01') & (self.data["Date"] <= '2022-12-31')]
        self.data = self.data.groupby(self.data["Date"].dt.to_period("M")).last()
        self.data.reset_index(drop=True, inplace=True)
        self.data.drop(columns=['Month', 'YYYY'], inplace=True)

        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        return self.data



michigansentiment = pd.read_csv("michigansentiment.csv")
michigansentiment_preprocessed = PreprocessMichiganSentiment(michigansentiment)
michigansentiment = michigansentiment_preprocessed.preprocess()


class PreprocessGDPGrowth:

    def __init__(self, data):
        self.data = data

    def preprocess(self):
        self.data = self.data.drop(columns = ["...1"])
        self.data["Date"] = pd.date_range(start="1992-01-01", periods=len(self.data), freq='ME')
        self.data = self.data[(self.data["Date"] >= '2012-01-01') & (self.data["Date"] <= '2022-12-31')]
        self.data = self.data[['Date', 'Monthly Real GDP Index']]

        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        return self.data

gdpgrowth = pd.read_csv("gdpgrowth.csv")
gdpgrowth_preprocessed = PreprocessGDPGrowth(gdpgrowth)
gdpgrowth = gdpgrowth_preprocessed.preprocess()


#Create final data frame
df = pd.DataFrame()

df.index = cpigrowth.index

df["price"] = portfolio_value.values
df["gdpgrowth"] = gdpgrowth["Monthly Real GDP Index"].values
df["cpigrowth"] = cpigrowth["USACPALTT01CTGYM"].values
df["unemp"] = unemploymentrate["UNRATE"].values
df["msci"] = michigansentiment["ICS_ALL"].values
df.to_csv('finalDF.csv', index=True)

