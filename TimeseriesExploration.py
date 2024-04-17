#This script performs a short preliminary analysis of the time series data at hand
# First section: visual inspection of all variables
# Second section: tests for stationarity, autocorrelation, and unit roots


import pandas as pd

df = pd.read_csv('finalDF.csv', index_col='Date', parse_dates=True)
dependent_var = df['price']

#Plotting time series
num_variables = len(df.columns)
fig, axes = plt.subplots(nrows=num_variables, ncols=1, figsize=(10, num_variables * 4))
if num_variables == 1:
    axes = [axes]
for ax, column in zip(axes, df.columns):
    ax.plot(df.index, df[column], label=f'{column}', marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel(column)
    ax.legend()

plt.tight_layout()
plt.show()
