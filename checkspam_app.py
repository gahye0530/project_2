# 스팸문자확인

import streamlit as st
import pandas as pd
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# 구두점과 불용어 제거하는 작업
def message_cleaning(Text) :
    test_punc_removed = [char for char in Text if char not in string.punctuation]
    # 하나의 문자열로 만듬
    test_punc_removed_join = ''.join(test_punc_removed)
    test_punc_removed_join_clean  = [word for word in test_punc_removed_join.split() if word.lower() not in my_stopwords]
    return test_punc_removed_join_clean

def run_checkspam() :
    spam_df = pd.read_csv('data/emails.csv')
    st.dataframe(spam_df)
    result = message_cleaning(spam_df.iloc[0,0])
    # st.write(spam_df.iloc[0,0])
    st.write(result)

    # training
    vectorizer = CountVectorizer(analyzer=message_cleaning)
    X = vectorizer.fit_transform(spam_df['text'])
    X = X.toarray()
    y = spam_df['spam']
    X_train, X_test, y_train, y_test = train_test_split(X, y)

