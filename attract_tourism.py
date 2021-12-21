import streamlit as st
from assortment_search import run_assort_search
from area_search import run_area_search
from name_search import run_name_search


def run_at() :
    choice = st.radio('',['지역별 검색', '구분별 검색', '관광지명 검색'])

    if choice == '지역별 검색' :
        run_area_search()
    elif choice == '구분별 검색' :
        run_assort_search()
    elif choice == '관광지명 검색' :
        run_name_search()