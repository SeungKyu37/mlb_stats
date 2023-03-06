import streamlit as st
import pandas as pd
import statsapi
from datetime import datetime
from streamlit_option_menu import option_menu

from home import run_home
from scores import run_scores
from stats import run_stats

choose = option_menu(None, ["Home", "Scores", "Stats"],
                         icons=['house', 'calendar', 'clipboard-data'],
                         menu_icon="app-indicator", default_index=0,
                         orientation='horizontal',
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "red", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "navy"},
}
)

if choose == "Home":
    run_home()

elif choose == "Scores":
    run_scores()
elif choose == "Stats":
    run_stats()
else:
    choose == "Home"