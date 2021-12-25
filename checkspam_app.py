# 스팸문자확인

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mysql.connector import errors

from mysql_connect import get_connection

spam_df = pd.read_csv('data/emails.csv')

def run_checkspam(vectorizer, classifier, my_stopwords) :
    st.subheader('Please enter your message')
    text = [st.text_area('','',height = 100, placeholder='Type here...')]

    if (st.button('확인')) & (text != '') :
        X_sample = vectorizer.transform(text)
        X_sample = X_sample.toarray()
        y_pred_sample = classifier.predict(X_sample)
        print(y_pred_sample[0].dtype)
        if y_pred_sample[0]==1 :
            st.write('Similar to messages previously identified as spam.')
            word_cloud(my_stopwords)
            result_send(text, 1)
        else :
            st.write('Not Spam.')
            word_cloud(my_stopwords)
            result_send(text, 0)

def result_send(text, spam) :
    st.subheader('분석결과를 서버로 보내주시겠습니까?')
    if st.button('Yes') :
        try :
            print('yyyyyeeeeeeesssssssss')
            connection = get_connection()
            query = '''insert into new_text(text, spam) values('%s',%s);'''
            record = (text, spam)
            cursor = connection.cursor()
            cursor.execute(cursor, record)
            connection.commit
        except errors as e :
            print('Error', e)
        finally :
            if connection.is_connected() :
                cursor.close()
                connection.close()
                st.write('Success')





# 워드클라우드
# pip install wordcloud
from wordcloud import WordCloud
from PIL import Image

def word_cloud(my_stopwords) :
    words_as_one_string = ''.join(spam_df['text'].tolist())
    img = Image.open('data/spam_img.JPG')
    img_mask = np.array(img)
    wc = WordCloud(background_color='white', mask = img_mask, stopwords = my_stopwords)
    wc.generate(words_as_one_string)

    fig = plt.figure()
    plt.imshow(wc)
    plt.axis('off')
    st.pyplot(fig)






