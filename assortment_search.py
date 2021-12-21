# 구분별검색
import streamlit as st
import pandas as pd
from draw_map import run_draw_map
def run_assort_search() :
    st.header('구분별 검색')
    df = pd.read_csv('data/tourism.csv')
    gubun_select = st.selectbox('구분검색', df['mcate_nm'].unique())
    map = df.loc[df['mcate_nm']==gubun_select, ['y','x']]
    df_select = df.loc[df['mcate_nm']==gubun_select,['poi_nm','mcate_nm','sido_nm','bemd_nm','ri_nm', 'beonji']]
    st.dataframe(df_select)
    run_draw_map(map)
