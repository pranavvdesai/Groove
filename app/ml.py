import numpy as np
import pandas as pd
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer

classifier=pickle.load(open('/home/abhash/Desktop/carpooling/hack_model/svc_clf2.pkl','rb'))
vectorizer=pickle.load(open('/home/abhash/Desktop/carpooling/hack_model/vec2.pkl','rb'))

def predict(tweet):
    # Takes input tweet , does all the preprocessing and gives prediction
    data=pd.DataFrame([],columns=['posts'])
    data.loc[0,'posts']=tweet
    formated_df = format_text(data,'posts')
    li=list(formated_df['posts'])
    tokenized=tknize_and_stop(li)
    stemmed=stem(tokenized)

    #use c_vec
    vector=vectorizer.transform(stemmed)

    #use classifier
    result=np.argmax(classifier.predict_proba(vector)[0])
    return result

def format_text(df,col):
    #Remove @ tags
    comp_df = df.copy()
    
    # remove all the punctuation
    comp_df[col] = comp_df[col].str.replace(r'(@\w*)','')

    #Remove URL
    comp_df[col] = comp_df[col].str.replace(r"http\S+", "")

    #Remove # tag and the following words
    comp_df[col] = comp_df[col].str.replace(r'#\w+',"")

    # Remove all non-character
    comp_df[col] = comp_df[col].str.replace(r"[^a-zA-Z ]","")

    # Remove extra space
    comp_df[col] = comp_df[col].str.replace(r'( +)'," ")
    comp_df[col] = comp_df[col].str.strip()

    # Change to lowercase
    comp_df[col] = comp_df[col].str.lower()

    return comp_df

def tknize_and_stop(tweet):
    tok_li=[]
    stop=set(stopwords.words('english'))
    for i in tweet:
        li=word_tokenize(i)
        stop_rem=[i for i in li if i not in stop]
        sen=" ".join(stop_rem)
        tok_li.append(sen)
    return tok_li

def stem(tweet):
    ss=SnowballStemmer('english')
    stem_sen=[]
    for i in tweet:
        sen=''
        wrds=i.split(' ')
        for j in wrds:
            w=ss.stem(j)
            sen+=w
            sen+=' '
        stem_sen.append(sen)
    return stem_sen  








