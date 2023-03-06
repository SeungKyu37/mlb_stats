import streamlit as st
import numpy as np
import pandas as pd
import statsapi
from datetime import datetime

from scores import hanguel

today = datetime.today().strftime("%m/%d/%Y")
scores = statsapi.schedule(start_date=today)

def today_score(index):
    away_team = hangeul(scores[index]["away_name"])
    away_score = scores[index]["away_score"]
    away_pitcher = scores[index]["away_probable_pitcher"]
    home_team = hanguel(scores[index]["home_name"])
    home_score = scores[index]["home_score"]
    home_pitcher = scores[index]["home_probable_pitcher"]
    inning = scores[index]["current_inning"]


def run_home():
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

    st.write(scores)

    