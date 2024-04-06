import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.stem import WordNetLemmatizer
#from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize,WhitespaceTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.corpus import wordnet


class TextPreprocessor:
    def toLower(self,text): #take input as string of text
        return text.lower()
    
    def removeSpecChar(self, text): #remove special char and num
        pattern = r'[^a-zA-Z\s]'
        cleaned_text = re.sub(pattern, "", text)
        return cleaned_text
    
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

    
    def remvStopwords(self, word_list): #take input as list of words
        stop_words = list(get_stop_words('en'))  
        nltk_words = list(stopwords.words('english')) 
        stop_words.extend(nltk_words)

        output = [word for word in word_list if not word in stop_words]

        return output


    def lemmatizate(self,word_list): #take input as list of words
        wnl = WordNetLemmatizer()
        output = [wnl.lemmatize(word) for word in word_list]

        return output
    
    def remvSynonyms(self, word_list): #take input as a list of words
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
    
   
    def tagPOS(self, word_list): ##take input as a list of words
       return  nltk.pos_tag(word_list)
           
           





def main():
    #download essential lib
    """
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    """
    #test with scrapped_articles.csv
    tp = TextPreprocessor()
    articles_df = pd.read_csv("./SalesEQ/scrapped_articles.csv",index_col = 0)[:500] 
    cleaned_data = {"newHeadline":[],"newText":[]}
    
    for i in range(len(articles_df)):  
        #lowercasing
        headline = tp.toLower(articles_df.loc[i,"Headline"])
        text = tp.toLower(articles_df.loc[i,"Text"])

        #remove special characters
        headline = tp.removeSpecChar(headline)
        text = tp.removeSpecChar(text)


        #tokenization
        headline = tp.tokenize(headline, mode = "w")
        text = tp.tokenize(text, mode = "w")

        #remove stopwords
        headline = tp.remvStopwords(headline)
        text = tp.remvStopwords(text)

        #lemmatize
        headline = tp.lemmatizate(headline)
        text = tp.lemmatizate(text)

        #remove synonym
        headline = tp.remvSynonyms(headline)
        text = tp.remvSynonyms(text)



        headline = " ".join(headline)
        text = " ".join(text)
        
        cleaned_data["newHeadline"].append(headline)
        cleaned_data["newText"].append(text)

    articles_df["newHeadline"] = cleaned_data["newHeadline"]
    articles_df["newText"] = cleaned_data["newText"]

    #print(articles_df)
    #articles_df.to_csv("./SalesEQ/result.csv",index = False)

        
   


    



if __name__ == '__main__':
    main()
    
