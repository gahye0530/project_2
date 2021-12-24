from numpy import place
import streamlit as st
import pandas as pd

from draw_map import run_draw_map

def run_name_search(df) :
    
    st.subheader('관광지명 검색')
    name = st.text_input('', placeholder='관광지명 입력')
    df_select = df.loc[df['poi_nm'].str.contains(name),['poi_nm','mcate_nm','sido_nm','bemd_nm','ri_nm', 'beonji']]
    if name != '' :
        map = df.loc[df['poi_nm'].str.contains(name), ['y','x']]
        run_draw_map(map)
        st.subheader('검색어 <{}>의 관광지 개수 : {}개' .format(name, map.shape[0]))
        chart_df = df.loc[df['poi_nm'].str.contains(name),'sido_nm'].value_counts()
        st.bar_chart(chart_df, width = 700, height = 500, use_container_width=False)
    st.dataframe(df_select)



 