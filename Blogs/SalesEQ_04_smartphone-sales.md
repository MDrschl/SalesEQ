---
Title: Dependent Data Selection (by Group "SalesEQ")
Date: 2024-04-23 22:00
Category: Progress Report
Tags: Group SalesEQ
---

### Main Contributer for this blog: Maximilian Droschl

## Reason for us to switch dependent variable

After evaluating several online sources for extracting monthly telephone sales data, including Capital IQ, Bloomberg and telephone company websites, our team realized that a standardized way of extracting the data was unrealistic. In order not to risk using poor quality data as the basis for our time series model to make the final prediction, the team concluded that it would be best to change the dependent variable.


## New dependent - Stock Price

To keep the focus on the American phone market, our new dependent variable will be the monthly return of a stock portfolio consisting of the five largest phone companies according to their market share within the American telecommunications market. According to Bloomberg, the companies with the largest market shares in the U.S. smartphone industry are Apple (68.23%), Samsung (25.20%), Motorola (3.90%), and Google (2.67%).


But why focus on stocks rather than phone sales? Financial markets, particularly stock markets, offer valuable insights into the performance of the smartphone industry. They are considered the most efficient means of reflecting all available information, regardless of its form of efficiency (Fama, 1970). In contrast to other performance measures, such as sales figures, profits, or expenses, financial markets provide a more comprehensive view. Accurately forecasting industry performance or the performance of a particular company within the industry can inform strategies for one's own business. Additionally, since companies have access to their own sales numbers, forecasted asset returns can serve as an informative explanatory variable in models aimed at forecasting sales.

However, Roberts (1967) demonstrated that there are various forms of efficiency that may lead to a pure approximation of future prices. This is because fundamental analysis relies on publicly available information and cannot generate excess returns. As the literature reports semi-strong form efficiency and occasional violations of it, we aim to provide more accurate forecasts by adding sentiment scores derived from our Sentiment-LDA model, in addition to publicly available information.


## Conclusion
In conclusion, the final time series model (ARIMAX/LSTM) will be fitted to the subsequent dataset: Dependent Variable - Monthly returns of equity portfolio; Explanatory Variables - Lagged returns of equity portfolio, Moving Average term, Residual term, Exogenous variables, which comprise the series of sentiment scores from our Sentiment-LDA model and the Michigan Consumer Sentiment Index.


## Reference
Fama, E. F. (1970). Efficient capital markets. Journal of finance, 25(2), 383-417.
 
Roberts, H. (1967). Statistical versus clinical prediction of the stock market CRSP. University of Chicago, Chicago.