# 구분별검색
import streamlit as st
import pandas as pd
from draw_map import run_draw_map
def run_assort_search(df) :
    st.header('구분별 검색')
    gubun_select = st.selectbox('', df['mcate_nm'].unique())
    map = df.loc[df['mcate_nm']==gubun_select, ['y','x']]
    df_select = df.loc[df['mcate_nm']==gubun_select,['poi_nm','mcate_nm','sido_nm','bemd_nm','ri_nm', 'beonji']]
    run_draw_map(map)
    
    st.subheader('전국 {} 관광지 개수 : {}개' .format(gubun_select, map.shape[0]))
    chart_df = df.loc[df['mcate_nm']==gubun_select,'sido_nm'].value_counts()

    # streamlit의 bar_chart를 이용하면 정렬이 안되고
    # dataframe의 plot을 이용하면 한글이 안먹히고..
    st.bar_chart(chart_df)
    st.dataframe(df_select)
