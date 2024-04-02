import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.stem import WordNetLemmatizer





class textPreprocessor:
    def toLower(self,text): #take input as a string of texts
        return text.lower()
    def tokenize(self,text):
        pass
    
    def removeStopwords(self, word_list): 
        nltk.download('stopwords')
        stop_words = list(get_stop_words('en'))         #About 900 stopwords
        nltk_words = list(stopwords.words('english')) #About 150 stopwords
        stop_words.extend(nltk_words)

        output = [word for word in word_list if not word in stop_words]

        return output


    def lemmatizate(self,word_list):
        nltk.download('wordnet')
        wnl = WordNetLemmatizer()
        word_list = ["I","am","going","home"]
        output = [wnl.lemmatize(word) for word in word_list]

        return output













def main():


  


if __name__ == '__main__':
    main()
    
