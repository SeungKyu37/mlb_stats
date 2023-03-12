import streamlit as st
import numpy as npname
import pandas as pd
import statsapi
from datetime import datetime, timedelta
from PIL import Image


from scores import hanguel

a= datetime.today()
y = a - timedelta(days=1)
y1 = y.strftime("%m/%d/%Y")

today = datetime.today().strftime("%m/%d/%Y")
scores = statsapi.schedule(start_date=today)

def team_img(team):
    if team == "Atlanta Braves":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/XY1SVEZwciGu2O0ChWKv4A_48x48.png'>"
    if team == 'Miami Marlins':
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/_dSQ2WYAxlh5bk1OEhPc_A_48x48.png'>"
    if team == 'New York Mets':
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/8VapQG4UqRE64iPYq6W3FQ_48x48.png'>"
    if team == "Philadelphia Phillies":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/DmFsZ1exRh9X0ZrTDt0Gaw_48x48.png'>"
    if team == 'Washington Nationals':
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/jEASG37S2n1Zeq8th2vEiA_48x48.png'>"
    if team == 'Chicago Cubs':
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/PBmgKhiGoYOGTl1L5FGaiQ_48x48.png'>"
    if team == "Cincinnati Reds":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/-XhGI3cGCeuXStm06CF_kw_48x48.png'>"
    if team == "Milwaukee Brewers":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/FGq_lQ42AmQDXXJOZ6ZOEA_48x48.png'>"
    if team == "Pittsburgh Pirates":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/9QU7ONeilzMGYb2AxTHzqA_48x48.png'>"
    if team == "St. Louis Cardinals":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/RM4q4pq8xBXC1OJths6qcQ_48x48.png'>"
    if team == "Arizona Diamondbacks":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/7s5ne5Cm_wPo5vBD9p7nRg_48x48.png'>"
    if team == "Colorado Rockies":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/Xhoba8Glkl5hAKLPis5WXQ_48x48.png'>"
    if team == "Los Angeles Dodgers":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/dgxxs-ybyRdTOEWRZ265AQ_48x48.png'>"
    if team == "San Diego Padres":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/asSCH0MODS0uEp8wzwIr9A_48x48.png'>"
    if team == "San Francisco Giants":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/Dg6bjCXwfLPYpZhI66005g_48x48.png'>"
    if team == "Baltimore Orioles":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/x8OiMUdBYnn-skDBvJX0ZQ_48x48.png'>"
    if team == "Boston Red Sox":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/PYjW8IShPc7b-aG2JX5p9w_48x48.png'>"
    if team == "New York Yankees":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/SvZBOWebmgQGdzqKGbYRCw_48x48.png'>"
    if team == "Tampa Bay Rays":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/_yTxeBZvNAZv5vl8BNjOvA_48x48.png'>"
    if team == "Toronto Blue Jays":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/7UyhGCGIKqafCLLaeRe8FA_48x48.png'>"
    if team == "Chicago White Sox":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/6qtJV1knLZtEZ8__xseKhA_48x48.png'>"
    if team == "Cleveland Guardians":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/eTgxG4yVCUpn1Tt_GUrIpA_48x48.png'>"
    if team == "Detroit Tigers":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/7rDj2EZVlcouQNkRgcxCmw_48x48.png'>"
    if team == "Kansas City Royals":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/9o_LwIzPvp46JyAcQdr7ow_48x48.png'>"
    if team == "Minnesota Twins":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/gBAstfK9v7682fKmomWeMA_48x48.png'>"
    if team == "Houston Astros":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/ey32o-rV1MBGbst3pFB_sg_48x48.png'>"
    if team == "Los Angeles Angels":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/o3IfXiKyLCntiZZGE8NPFw_48x48.png'>"
    if team == "Oakland Athletics":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/AJKr46qzAlyyzvI1sL1CbQ_48x48.png'>"
    if team == "Seattle Mariners":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/CcJYNnWBPQcT-lP1fUIf8Q_48x48.png'>"
    if team == "Texas Rangers":
        image = "<img src='https://ssl.gstatic.com/onebox/media/sports/logos/htC4FWpoeXLC_qW-UyoUSA_48x48.png'>"
    return image

def game(type_game):
    if type_game == "W":
        game_type = "월드시리즈"
    if type_game == "L":
        game_type = "리그챔피언십"
    if type_game == "D":
        game_type = "디비전시리즈"
    if type_game == "F":
        game_type = "와일드카드시리즈"
    if type_game == "R":
        game_type = "정규시즌"
    if type_game == "S":
        game_type = "프리시즌"
    return game_type

def today_score(index):
    try:
        away_team = scores[index]["away_name"]
        away_team2 = hanguel(scores[index]["away_name"])
        away_score = scores[index]["away_score"]
        away_pitcher = scores[index]["away_probable_pitcher"]
        home_team = scores[index]["home_name"]
        home_team2 = hanguel(scores[index]["home_name"])
        home_score = scores[index]["home_score"]
        home_pitcher = scores[index]["home_probable_pitcher"]
        inning = scores[index]["current_inning"] + "회"
        if inning == "회":
            inning = ""
        game_type = scores[index]["game_type"]
        game_type = game(game_type)
        status = scores[index]["status"]
        if status == "Final":
            status1 = "종료"
        elif status == "Scheduled":
            status1 = "예정"
        else:
            status1 = "진행중"

        html = f"""
            <style>
                table, tr, td {{
                    border: none;
                }}
            </style>
            <table border = "4">
                <tr>
                    <td colspan = "4">{game_type}</td>
                </tr>
                <tr>
                    <td>{team_img(away_team)}</td>
                    <td>{away_team2}</td>
                    <td>{away_score}</td>
                    <td rowspan = "3">{status1}<br>{inning}</td>
                </tr>
                <tr>
                    <td>{team_img(home_team)}</td>
                    <td>{home_team2}</td>
                    <td>{home_score}</td>
                </tr>
            </table><br>
        """
        return st.markdown(html, unsafe_allow_html=True)
    except:
        pass

def run_home():

    st.title("오늘의 경기결과")
    col0, col1 = st.columns(2)
    with col0:
        today_score(0)
        today_score(2)
        today_score(4)
        today_score(6)
        today_score(8)
        today_score(10)
        today_score(12)
        today_score(14)
        today_score(16)
        today_score(18)
        today_score(20)
        today_score(22)
        today_score(24)
        today_score(26)
        today_score(28)

    with col1:
        today_score(1)
        today_score(3)
        today_score(5)
        today_score(7)
        today_score(9)
        today_score(11)
        today_score(13)
        today_score(15)
        today_score(17)
        today_score(19)
        today_score(21)
        today_score(23)
        today_score(25)
        today_score(27)
        today_score(29)

    


    