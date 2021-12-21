import streamlit as st

def run_draw_map(map_df) :
    map_df.rename(columns = {'y' : 'lat', 'x' : 'lon'}, inplace = True)
    st.map(map_df)