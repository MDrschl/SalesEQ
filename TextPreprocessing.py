import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize,WhitespaceTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer
from nltk.corpus import wordnet


class TextPreprocessor:
    def toLower(self,text): #take input as string of text
        return text.lower()
    
    def tokenize(self,text,mode):
        if mode == "ws": #whitespace
            return text.split()
        elif mode == "l": #line
            return nltk.sent_tokenize(text)
        elif mode == "w": #word
            return nltk.word_tokenize(text)
        elif mode == "p": #punctuation base
            return nltk.wordpunct_tokenize(text)
        else: #treebankword
            tokenizer = TreebankWordTokenizer()
            return tokenizer.tokenize(text)

    
    def removeStopwords(self, word_list): #take input as list of words
        nltk.download('stopwords')
        stop_words = list(get_stop_words('en'))  
        nltk_words = list(stopwords.words('english')) 
        stop_words.extend(nltk_words)

        output = [word for word in word_list if not word in stop_words]

        return output


    def lemmatizate(self,word_list): #take input as list of words
        nltk.download('wordnet')
        wnl = WordNetLemmatizer()
        output = [wnl.lemmatize(word) for word in word_list]

        return output
    
    def removeSynonyms(self, word_list): #take input as a list of words
        syns = []
        for i in range(len(word_list)):
            if word_list[i] in set(syns): #the word is a synonym of other words appeared before
                word_list[i] = ""

            else: 
                #find synonyms
                for s in wordnet.synsets(word_list[i]):
                    for lem in s.lemmas():
                        syns.append(lem.name())
        return  list(filter(lambda a: a != "", word_list))
       
           







def main():
    pass

  


if __name__ == '__main__':
    main()
    
