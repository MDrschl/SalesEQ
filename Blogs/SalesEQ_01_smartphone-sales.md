---
Title: Project Introduction – Predicting Smartphone Sales in the United States (by Group "SalesEQ")
Date: 2024-03-04 18:00
Category: Progress Report
Tags: Group SalesEQ
---


## Group Members

Zixian Fan, majoring in Statistics, with a second major in Finance, and a minor in Computer Science. Loves math, loves quantitative research, and has a sweet tooth. Loves to play games, with previously being in the Legends segment of Hearthstone.
[https://github.com/FanZixian](https://github.com/FanZixian)

Maximilian Droschl, Bachelor in Economics with focus on Econometrics and Data Science, Exchange Student from the University of St. Gallen. Has a passion for chess and loves playing lacrosse. 
[https://github.com/MDrschl](https://github.com/MDrschl)

Ricky Choi, double degree in Computer Science and Finance at HKU. Loves teamsports, working out, and playing snooker. Also enjoys watching movies and animes. 
[https://github.com/Rickycmk](https://github.com/Rickycmk)

Jason Li, majoring in Quantitative Finance and minoring in Computer Science. Loves playing sports like volleyball and football. Also a lover of sitcoms and movies.
[https://github.com/Jasonlcyy](https://github.com/Jasonlcyy)

Mahir Faiaz, Bachelor of Arts and Sciences in Financial Technology. An avid international debater and a silly soccer lover.
[https://github.com/MahirFaiaz](https://github.com/MahirFaiaz)



## Objective of this blog

This blogpost is intended to provide a surface-level idea about the ins and outs of our project. We will elaborate on the exact objective of our project, and then illustrate possible mechanisms to reach our end goals. As we do that, we will also be discussing the viability of our proposed methods and our targeted data sources.

This blogpost is designed to allow the reader to get a good insight into the types of discussions we indulged in to get to this stage of the project. We believe such a practice will allow the reader to get a deeper understanding of our motivations and the ability to grasp what events led to a given outcome. In the long run, this should give the Professor a proper timeline of our project and an idea about the group atmosphere at any given point in the timeline, leading to the possibility of a more comprehensive evaluation.



## Outline of the Project

The overarching objective of our project will be to predict smartphone sales in the United States. This is primarily motivated by the fact that the smartphone industry has become increasingly competitive in recent years, forcing manufacturers to develop new strategies. One of these strategies is forecasting industry sales, which, if mismanaged, can have significant consequences. The rapid pace of product development, increasing differentiation among smartphones, and relatively short life cycles of smartphones contribute to unpredictable sales patterns and increased volatility, exacerbating the challenge. Traditional models are mostly based on past values of the sales series itself, variables related to the product, such as its price or the brand, consumer sentiment indices, and economic variables such as the consumer price index or stock indices. However, we are motivated to extend these traditional techniques to a hybrid forecasting model that aims to incorporate sentiment indices estimated on the basis of text data related to phone sales. Thereby, we test the hypothesis whether sentiment scores derived from news articles add predictive information to traditional model specifications.


## Modeling and data scraping

In general, our approach employs three different models. An LDA model is used to properly extract information from large amounts of text data with content related to smartphone sales in the United States. The final prediction is then made by an ARIMAX model, which has the advantage of being able to interpret the significance of each predictor variable included in the model, while at the same time allowing the modeling of non-stationary multivariate data. For comparison reasons, an LSTM model will be fitted to the data.

Note that we haven’t decided which text data to be included in our research, because it is not determined what websites, articles, forums are available for web scraping or whether these data are easy to process and effective to our model. Even after narrowing down the scope, the reliability and relevance of these sources are not necessarily ensured. The source and the effective method to query reliable and relevant articles/tweets are problems that need to be sorted. Although, we would like to mention some text data candidates that might be applied in our text analysis:

Seeking Alpha
Twitters
Some articles from free financial journals

Additionally, as the data is not determined yet, we cannot give the name of our exogenous variables that will be applied to the ARIMAX/LSTM model. Hence, they are also not included in this blog post, but will be included in our following blogs soon as soon as we have fitted them to the data.

## Reference
Farkhod, A., Abdusalomov, A., Makhmudov, F., & Cho, Y. I. (2021). LDA-Based Topic Modeling Sentiment Analysis Using Topic/Document/Sentence (TDS) Model. Applied Sciences, 11(23), 11091.

Ali, T., Omar, B., & Soulaimane, K. (2022). Analyzing Tourism Reviews Using an LDA Topic-Based Sentiment Analysis Approach. MethodsX, 101894.

Sa-Ngasoongsong, A., Bukkapatnam, S. T., Kim, J., Iyer, P. S., & Suresh, R. P. (2012). Multi-step sales forecasting in automotive industry based on structural relationship identification. International Journal of Production Economics, 140(2), 875-887.

Hwang, S., Yoon, G., Baek, E., & Jeon, B. K. (2023). A Sales Forecasting Model for New-Released and Short-Term Product: A Case Study of Mobile Phones. Electronics, 12(15), 3256.

Jadhav, T. (2020). Prediction of Cell Phone Sales from Online Reviews Using Text Mining. International Journal of Research in Engineering, Science and Management, 3(8), 214-218.

Lassen, N. B., Madsen, R., & Vatrapu, R. (2014, September). Predicting iphone sales from iphone tweets. In 2014 IEEE 18th International Enterprise Distributed Object Computing Conference (pp. 81-90). IEEE.


