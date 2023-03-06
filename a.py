import streamlit as st
import pandas as pd
import statsapi
from datetime import datetime


date = st.sidebar.date_input('날짜 선택')
date = date.strftime("%m/%d/%Y")
st.sidebar.write("팀 선택")
league = st.sidebar.selectbox('리그 선택',('내셔널 리그', '아메리칸 리그'))
region = st.sidebar.selectbox('지구 선택',('동부', '중부', '서부'))
if league == '내셔널 리그' & region == '동부':
    team = st.sidebar.selectbox('팀선택', ('애틀랜타 브레이브스', '마이애미 말린스', '뉴욕 매츠', '필라델피아 필리스', '워싱턴 내셔널스'))