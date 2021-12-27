# 스팸문자확인

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mysql.connector import errors
from wordcloud.wordcloud import STOPWORDS

from mysql_connect import get_connection

# 워드클라우드
# pip install wordcloud
from wordcloud import WordCloud
from PIL import Image

spam_df = pd.read_csv('data/emails.csv')

def word_cloud() :
    my_stopwords = STOPWORDS
    words_as_one_string = ''.join(spam_df.loc[spam_df['spam']==1,'text'].tolist())
    img = Image.open('data/spam_img.JPG')
    img_mask = np.array(img)
    my_stopwords.add('Subject')
    my_stopwords.add('us')
    my_stopwords.add('one')
    wc = WordCloud(background_color='white', mask = img_mask, stopwords = my_stopwords)
    wc.generate(words_as_one_string)

    fig = plt.figure()
    plt.imshow(wc)
    plt.axis('off')
    st.pyplot(fig)
spam=0
def run_checkspam(vectorizer, classifier) :
    st.subheader('Please enter your message')
    # 학습을 위해 리스트 형태로 가져온다. 
    st.write('scaler : CountVectorizer / modeling : multinomialNB')
    text = [st.text_area('','',height = 100, placeholder='Type here in english...')]
    if (st.button('확인')) & (text != '') :
        X_sample = vectorizer.transform(text)
        X_sample = X_sample.toarray()
        y_pred_sample = classifier.predict(X_sample)
        global spam
        if y_pred_sample[0]==1 :
            st.subheader('Similar to messages previously identified as spam.')
            spam=1
        else :
            st.subheader('Not Spam.')
            spam=0
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    # 리스트 형태로 가지고 온 text를 문자열 형태로 result_send함수를 호출한다. 
    # 텍스트를 apply하거나 버튼하나를 눌러도 새로고침돼서 spam결과를 보내기 어렵다. 
    result_send(text[0], spam)
    

def result_send(text, spam) :
    st.write('Transmission of analysis results?')
    if st.button('Yes') :
        try :
            connection = get_connection()
            query ='''insert into new_text(text, spam) values(%s,%s);'''
            record= (text,spam)
            cursor = connection.cursor()
            cursor.execute(query, record)
            connection.commit()
        except errors as e :
            print('Error', e)
        finally :
            if connection.is_connected() :
                cursor.close()
                connection.close()
                # st.write('Success')
                word_cloud()