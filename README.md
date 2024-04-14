# SalesEQ
Introducing ourselves, team SalesEQ

Zixian Fan, majoring in Statistics, with a second major in Finance, and a minor in Computer Science. Loves math, loves quantitative research, and has a sweet tooth. Currently jobless, and loves to play games, with previously being in the Legends segment of Hearthstone.
https://github.com/FanZixian

Maximilian Droschl, Bachelor in Economics with focus on Econometrics and Data Science, Exchange Student from the University of St. Gallen. Has a passion for chess and loves playing lacrosse. 
https://github.com/MDrschl

Ricky Choi, double degree in Computer Science and Finance at HKU. Loves teamsports, working out, and playing snooker. Also enjoys watching movies and animes. 
https://github.com/Rickycmk

Jason Li, majoring in Quantitative Finance and minoring in Computer Science. Loves playing sports like volleyball and football. Also a lover of sitcoms and movies.
https://github.com/Jasonlcyy

Mahir Faiaz, Bachelor of Arts and Sciences in Financial Technology. An avid international debater and a silly soccer lover.
https://github.com/MahirFaiaz


Outline of the Project:

The overarching objective of our project will be to predict smartphone sales in the United States. This is primarily motivated by the fact that the smartphone industry has become increasingly competitive in recent years, forcing manufacturers to develop new strategies. One of these strategies is forecasting industry sales, which, if mismanaged, can have significant consequences. The rapid pace of product development, increasing differentiation among smartphones, and relatively short life cycles of smartphones contribute to unpredictable sales patterns and increased volatility, exacerbating the challenge. Traditional models are mostly based on past values of the sales series itself, variables related to the product, such as its price or the brand, consumer sentiment indices, and economic variables such as the consumer price index or stock indices. However, we are motivated to extend these traditional techniques to a hybrid forecasting model that aims to incorporate sentiment indices estimated on the basis of text data related to phone sales. Thereby, we test the hypothesis whether sentiment scores derived from news articles add predictive information to traditional model specifications.

## Dataset
Our full dataset is stored in the [google drive](https://drive.google.com/drive/folders/1t0VqvahJ8TU7xbR--bmxS6kswSmw0B1r?usp=sharing). You can download the data from this link and put it with the following path:



## Run the sentiment LDA
To run the sentiment LDA model, you first need to download the dictionary `sentiwordnet` from `nltk`:

```
import nltk
nltk.download('sentiwordnet')
```

### Run the sample trial in the reference repo
The code has already been adjusted to make sure it works for the current packages versions. Simply run the code of `amazon_trail.ipynb` can provide the top25 positive and negative words from the given datasets.
