# 지역별검색
import streamlit as st
import pandas as pd
from draw_map import run_draw_map
import matplotlib.pyplot as plt


def run_area_search() :

    st.header('지역별 검색')
    df = pd.read_csv('data/tourism.csv')
    sido_select = st.selectbox('시·도 검색', df['sido_nm'].unique())
    sgg = df.loc[df['sido_nm']==sido_select, 'sgg_nm'].unique()
    sgg_select = st.selectbox('구·군 검색', sgg)
    condition = (df['sido_nm']==sido_select) & (df['sgg_nm']==sgg_select)
    map = df.loc[condition, ['y','x']]
    run_draw_map(map)
    st.subheader('{} {} 관광지 개수 : {}개' .format(sido_select, sgg_select, map.shape[0]))
    chart_df = df.loc[condition,'mcate_nm'].value_counts()

    # streamlit의 bar_chart를 이용하면 정렬이 안되고
    # dataframe의 plot을 이용하면 한글이 안먹히고..
    st.bar_chart(chart_df)
    