import streamlit as st
import pandas as pd

def draw_map(map_df) :
    map_df.rename(columns = {'y' : 'lat', 'x' : 'lon'}, inplace = True)
    st.map(map_df)

def main() :
    df = pd.read_csv('data/tourism.csv')
    
    draw_map(df[['y', 'x']])

    st.subheader('지역검색')

    sido_select = st.selectbox('시·도 검색', df['sido_nm'].unique())
    sgg = df.loc[df['sido_nm']==sido_select, 'sgg_nm'].unique()
    sgg_select = st.selectbox('시·구·군 검색', sgg)






    map = df.loc[df['sido_nm']==sido_select, ['y','x']]
    draw_map(map)

    
if __name__ == '__main__' : main()