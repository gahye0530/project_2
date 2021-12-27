import streamlit as st
import pandas as pd
from assortment_search import run_assort_search
from area_search import run_area_search
from name_search import run_name_search


def run_at() :
    df = pd.read_csv('data/tourism.csv')
    st.write('데이터 출처 : 문화빅데이터 포털사이트 - 국내 지역별 관광명소데이터 (2021)')
    choice = st.radio('',['지역별 검색', '구분별 검색', '관광지명 검색'])

    if choice == '지역별 검색' :
        run_area_search(df)
    elif choice == '구분별 검색' :
        run_assort_search(df)
    elif choice == '관광지명 검색' :
        run_name_search(df)