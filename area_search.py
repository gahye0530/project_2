# 지역별검색
import streamlit as st
import pandas as pd
from draw_map import run_draw_map


def run_area_search() :

    st.header('지역별 검색')
    df = pd.read_csv('data/tourism.csv')
    sido_select = st.selectbox('시·도 검색', df['sido_nm'].unique())
    sgg = df.loc[df['sido_nm']==sido_select, 'sgg_nm'].unique()
    sgg_select = st.selectbox('시·구·군 검색', sgg)
    condition = (df['sido_nm']==sido_select) & (df['sgg_nm']==sgg_select)
    map = df.loc[condition, ['y','x']]
    run_draw_map(map)