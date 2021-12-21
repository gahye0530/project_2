import streamlit as st
import pandas as pd

from draw_map import run_draw_map

def run_name_search() :
    df = pd.read_csv('data/tourism.csv')
    name = st.text_input('관광지명 입력')
    df_select = df.loc[df['poi_nm'].str.contains(name),['poi_nm','mcate_nm','sido_nm','bemd_nm','ri_nm', 'beonji']]
    st.dataframe(df_select)
    map = df.loc[df['poi_nm'].str.contains(name), ['y','x']]
    run_draw_map(map)