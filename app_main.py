import streamlit as st
import pandas as pd
from attract_tourism import run_at
from checkspam_app import run_checkspam
import joblib
import string
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')

# 구두점과 불용어 제거하는 작업
def message_cleaning(Text) :
    test_punc_removed = [char for char in Text if char not in string.punctuation]
    # 하나의 문자열로 만듬
    test_punc_removed_join = ''.join(test_punc_removed)
    test_punc_removed_join_clean  = [word for word in test_punc_removed_join.split() if word.lower() not in my_stopwords]
    return test_punc_removed_join_clean

def main() :
    # 피클파일로 가지고 오면 정확도 산출이 어렵다. 
    vectorizer = joblib.load('data/vectorizer.pkl')
    classifier = joblib.load('data/classifier1.pkl')
    choice = st.sidebar.selectbox('검색선택',['국내 관광 명소', 'SPAM 문자 확인'])

    if choice == '국내 관광 명소' :
        run_at()
    elif choice == 'SPAM 문자 확인' :
        run_checkspam(vectorizer, classifier) 
        
    
if __name__ == '__main__' : main()