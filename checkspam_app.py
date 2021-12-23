# 스팸문자확인

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
spam_df = pd.read_csv('data/emails.csv')

# 구두점과 불용어 제거하는 작업
def message_cleaning(Text) :
    test_punc_removed = [char for char in Text if char not in string.punctuation]
    # 하나의 문자열로 만듬
    test_punc_removed_join = ''.join(test_punc_removed)
    test_punc_removed_join_clean  = [word for word in test_punc_removed_join.split() if word.lower() not in my_stopwords]
    return test_punc_removed_join_clean

def run_checkspam() :
    
    # training
    # 카운트벡터라이저의 애널라이저 파라미터를 설정해주면 함수를 실행 후 숫자로 변경해준다. 
    vectorizer = CountVectorizer(analyzer=message_cleaning)
    X = vectorizer.fit_transform(spam_df['text'])
    X = X.toarray()
    y = spam_df['spam']
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    # 정확도 산출
    accuracy = accuracy_score(y_test, y_pred)
    print('정확도 : {}%' .format(round(accuracy,2)))

    st.subheader('Please enter your message')
    text = [st.text_area('','',height = 100, placeholder='Type here...')]

    if (st.button('확인')) & (text != '') :
        X_sample = vectorizer.transform(text)
        X_sample = X_sample.toarray()
        y_pred_sample = classifier.predict(X_sample)
        if y_pred_sample[0]=='1' :
            st.write('Similar to messages previously identified as spam. (정확도 : {}%)' .format(round(accuracy,2)*100))
            result_send(text, 1)
        else :
            st.write('Not Spam (정확도 : {}%)' .format(round(accuracy,2)*100))
            result_send(text, 0)

def result_send(text, spam) :
    word_cloud()
    st.subheader('분석결과를 서버로 보내주시겠습니까?')
    if st.button('Yes') :
        test = spam_df.append({'text' : text, 'spam' : spam}, ignore_index=True)
        test.to_csv('data/test.csv')


# 워드클라우드
# pip install wordcloud
import streamlit_wordcloud
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

def word_cloud() :
    words_as_one_string = ''.join(spam_df['text'].tolist())
    img = Image.open('data/spam_img.JPG')
    img_mask = np.array(img)
    wc = WordCloud(background_color='white', mask = img_mask, stopwords = my_stopwords)
    wc.generate(words_as_one_string)

    fig = plt.figure()
    plt.imshow(wc)
    plt.axis('off')
    st.pyplot(fig)






