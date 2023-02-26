import streamlit as st
import pandas as pd
import numpy as np
import statsapi
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
f = [f.name for f in fm.fontManager.ttflist]
print(f)

# 확인 이후
plt.rc('font', family='Malgun Gothic')
# from matplotlib import font_manager, rc
# font_path = "./font/MALGUN.TTF"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

def hanguel(team):
    if team == "Atlanta Braves":
        name = '애틀랜타'
    if team == 'Miami Marlins':
        name = '마이애미'
    if team == 'New York Mets':
        name = '뉴욕 메츠'
    if team == "Philadelphia Phillies":
        name = '필라델피아'
    if team == 'Washington Nationals':
        name = '워싱턴'
    if team == 'Chicago Cubs':
        name = '시카고 컵스'
    if team == "Cincinnati Reds":
        name = '신시내티'
    if team == "Milwaukee Brewers":
        name = '밀워키'
    if team == "Pittsburgh Pirates":
        name = '피츠버그'
    if team == "St. Louis Cardinals":
        name = '세인트루이스'
    if team == "Arizona Diamondbacks":
        name = '애리조나'
    if team == "Colorado Rockies":
        name = '콜로라도'
    if team == "Los Angeles Dodgers":
        name = 'LA다저스'
    if team == "San Diego Padres":
        name = '샌디에이고'
    if team == "San Francisco Giants":
        name = '샌프란시스코'
    if team == "Baltimore Orioles":
        name = '볼티모어'
    if team == "Boston Red Sox":
        name = '보스턴'
    if team == "New York Yankees":
        name = '뉴욕 양키스'
    if team == "Tampa Bay Rays":
        name = '템파베이'
    if team == "Toronto Blue Jays":
        name = '토론토'
    if team == "Chicago White Sox":
        name = '시카고W'
    if team == "Cleveland Guardians":
        name = '클리블랜드'
    if team == "Detroit Tigers":
        name = '디트로이트'
    if team == "Kansas City Royals":
        name = '캔자스시티'
    if team == "Minnesota Twins":
        name = '미네소타'
    if team == "Houston Astros":
        name = '휴스턴'
    if team == "Los Angeles Angels":
        name = 'LA에인절스'
    if team == "Oakland Athletics":
        name = '오클랜드'
    if team == "Seattle Mariners":
        name = '시애틀'
    if team == "Texas Rangers":
        name = '텍사스'
    return name
    

def run_scores():
    # today = datetime.today().strftime("%m/%d/%Y")

    date = st.sidebar.date_input('날짜 선택')
    st.sidebar.write("팀 선택")
    league = st.sidebar.selectbox('리그 선택',('내셔널 리그', '아메리칸 리그'))
    if league == '내셔널 리그':
        region = st.sidebar.selectbox('지구 선택',('동부', '중부', '서부'))
        if region == '동부':
            team = st.sidebar.selectbox('팀선택', ('애틀랜타 브레이브스', '마이애미 말린스', '뉴욕 매츠', '필라델피아 필리스', '워싱턴 내셔널스'))
        elif region == '중부':
            team = st.sidebar.selectbox('팀선택', ('시카고 컵스', '신시내티 레즈', '밀워키 브루어스', '피츠버그 파이리츠', '세인트루이스 카디널스'))
        elif region == '서부':
            team = st.sidebar.selectbox('팀선택', ('애리조나 다이아몬드백스', '콜로라도 로키스', '로스앤젤레스 다저스', '샌디에이고 파드리스', '샌프란시스코 자이언츠'))
    elif league == '아메리칸 리그':
        region = st.sidebar.selectbox('지구 선택',('동부', '중부', '서부'))        
        if region == '동부':
            team = st.sidebar.selectbox('팀선택', ('볼티모어 오리올스', '보스턴 레드삭스', '뉴욕 양키스', '템파베이 레이스', '토론토 블루제이스'))
        elif region == '중부':
            team = st.sidebar.selectbox('팀선택', ('시카고 화이트삭스', '클리블랜드 가디언스', '디트로이트 타이거스', '캔자스시티 로열스', '미네소타 트윈스'))
        elif region == '서부':
            team = st.sidebar.selectbox('팀선택', ('휴스턴 애스트로스', '로스앤젤레스 에인절스', '오클랜드 애슬레틱스', '시애틀 매리너스', '텍사스 레인저스'))
   
    if team == '애틀랜타 브레이브스':
        team_id = 144
    elif team == '마이애미 말린스':
        team_id = 146
    elif team == '뉴욕 매츠':
        team_id = 121
    elif team == '필라델피아 필리스':
        team_id = 143
    elif team == '워싱턴 내셔널스':
        team_id = 120
    elif team == '시카고 컵스':
        team_id = 112
    elif team == '신시내티 레즈':
        team_id = 113
    elif team == '밀워키 브루어스':
        team_id = 158
    elif team == '피츠버그 파이리츠':
        team_id = 134
    elif team == '세인트루이스 카디널스':
        team_id = 138
    elif team == '애리조나 다이아몬드백스':
        team_id = 109
    elif team == '콜로라도 로키스':
        team_id = 115
    elif team == '로스앤젤레스 다저스':
        team_id = 119
    elif team == '샌디에이고 파드리스':
        team_id = 135
    elif team == '샌프란시스코 자이언츠':
        team_id = 137
    elif team == '볼티모어 오리올스':
        team_id = 110
    elif team == '보스턴 레드삭스':
        team_id = 111
    elif team == '뉴욕 양키스':
        team_id = 147
    elif team == '템파베이 레이스':
        team_id = 139
    elif team == '토론토 블루제이스':
        team_id = 141
    elif team == '시카고 화이트삭스':
        team_id = 145
    elif team == '클리블랜드 가디언스':
        team_id = 114
    elif team == '디트로이트 타이거스':
        team_id = 116
    elif team == '캔자스시티 로열스':
        team_id = 118
    elif team == '미네소타 트윈스':
        team_id = 142
    elif team == '휴스턴 애스트로스':
        team_id = 117
    elif team == '로스앤젤레스 에인절스':
        team_id = 108
    elif team == '오클랜드 애슬레틱스':
        team_id = 133
    elif team == '시애틀 매리너스':
        team_id = 136
    elif team == '텍사스 레인저스':
        team_id = 140

    date = date.strftime("%m/%d/%Y")
    scores = statsapi.schedule(start_date=date,team=team_id)
    # st.write(scores)

    try:
        game_id = scores[0]['game_id']

        # 라인스코어
        linescore = statsapi.linescore(game_id)
        # st.write(linescore)
        line = linescore.split("\n")
        line1 = line[0].split()
        line2 = line[1].split()
        line3 = line[2].split()
        def insert(line):
            if line[0] == 'Red':
                del line[1]
                del line[0]
                line.insert(0, 'RedSox')
            elif line[0] == 'White':
                del line[1]
                del line[0]
                line.insert(0, 'WhiteSox')
            elif line[0] == 'Blue':
                del line[1]
                del line[0]
                line.insert(0, 'BlueJays')
            return line

        line2 = insert(line2)
        line3 = insert(line3)

        if line1[10] != 'R': 
            l10 = line1[10]
            li = ' '.join([l10[i:i+2] for i in range(0, len(l10), 2)])
            l10 = li.split(' ')
            del line1[10]

            
            for a in range(int(l10[0]), int(l10[0])+int(len(l10))):
                line1.insert(a, l10[a-10])
        

        df_score = pd.DataFrame(columns=line1)
        df_score.loc[0] = line2
        df_score.loc[1] = line3
        df_score = df_score.set_index('Final')

        
        away = scores[0]['away_name']
        home = scores[0]['home_name']
        away_h = hanguel(away)
        home_h = hanguel(home)
        away_score = str(scores[0]['away_score'])
        home_score = str(scores[0]['home_score'])
        st.title(away_h + away_score + " " + home_score + home_h)
        st.write(df_score)

        boxscore = statsapi.boxscore_data(game_id)
        # st.write(boxscore)
        away_hits = boxscore['away']['teamStats']['batting']['hits']
        away_hrs = boxscore['away']['teamStats']['batting']['homeRuns']
        away_stolen = boxscore['away']['teamStats']['batting']['stolenBases']
        away_so = boxscore['away']['teamStats']['batting']['strikeOuts']
        away_lob = boxscore['away']['teamStats']['batting']['leftOnBase']

        home_hits = boxscore['home']['teamStats']['batting']['hits']
        home_hrs = boxscore['home']['teamStats']['batting']['homeRuns']
        home_stolen = boxscore['home']['teamStats']['batting']['stolenBases']
        home_so = boxscore['home']['teamStats']['batting']['strikeOuts']
        home_lob = boxscore['home']['teamStats']['batting']['leftOnBase']

        a = ['안타', '홈런', '도루', '삼진', '잔루']
        b = np.array([away_hits, away_hrs, away_stolen, away_so, away_lob])
        c = np.array([home_hits, home_hrs, home_stolen, home_so, home_lob])

        y = np.arange(c.size)
        

        fig, axes = plt.subplots(ncols=2, sharey=True)
        
        axes[0].barh(y, b, align='center', color='navy', zorder=10)
        axes[0].set(title=away_h)
        axes[1].barh(y, c, align='center', color='navy', zorder=10)
        axes[1].set(title=home_h)

        axes[0].invert_xaxis()
        axes[0].invert_yaxis()
        axes[0].set(yticks=y, yticklabels=a)
        axes[0].yaxis.tick_right()

        axes[0].spines['top'].set_visible(False)
        axes[0].spines['right'].set_visible(False)
        axes[0].spines['left'].set_visible(False)
        axes[0].spines['bottom'].set_visible(False)
        axes[1].spines['top'].set_visible(False)
        axes[1].spines['right'].set_visible(False)
        axes[1].spines['left'].set_visible(False)
        axes[1].spines['bottom'].set_visible(False)
        fig.set_figheight(2)
        fig.tight_layout()
        fig.subplots_adjust(wspace=0.165)
        st.pyplot(fig)

        def batting_stats(home_away):
            boxscore = statsapi.boxscore_data(game_id)

            batter = boxscore[home_away]['batters']
            batter_list = []
            for i in range(len(batter)):
                batter_list.append(batter[i])

            batting_df = pd.DataFrame(columns=['타자명','타수', '득점', '안타', '타점', '홈런', '볼넷', '삼진', '타율'])
            
            for i in range(len(batter_list)):
                try:
                    name = boxscore[home_away]['players']['ID'+str(batter_list[i])]['person']['fullName']
                    atBats = boxscore[home_away]['players']['ID'+str(batter_list[i])]['stats']['batting']['atBats']
                    runs = boxscore[home_away]['players']['ID'+str(batter_list[i])]['stats']['batting']['runs']
                    hits = boxscore[home_away]['players']['ID'+str(batter_list[i])]['stats']['batting']['hits']
                    rbi = boxscore[home_away]['players']['ID'+str(batter_list[i])]['stats']['batting']['rbi']
                    homeRuns = boxscore[home_away]['players']['ID'+str(batter_list[i])]['stats']['batting']['homeRuns']
                    baseOnBalls = boxscore[home_away]['players']['ID'+str(batter_list[i])]['stats']['batting']['baseOnBalls']
                    strikeOuts = boxscore[home_away]['players']['ID'+str(batter_list[i])]['stats']['batting']['strikeOuts']
                    avg = boxscore[home_away]['players']['ID'+str(batter_list[i])]['seasonStats']['batting']['avg']
                    batting_df.loc[i] = [name, atBats, runs, hits, rbi, homeRuns, baseOnBalls, strikeOuts, avg]
                except:
                    pass    
            batting_df = batting_df.set_index("타자명")
            return batting_df

        def pitching_stats(home_away):
            boxscore = statsapi.boxscore_data(game_id)
            pitcher = boxscore[home_away]['pitchers']
            pitcher_list = []
            for i in range(len(pitcher)):
                pitcher_list.append(pitcher[i])

            pitching_df = pd.DataFrame(columns=['투수명', '이닝', '피안타', '자책', '볼넷', '삼진', '투구수', '평균자책'])

            for i in range(len(pitcher_list)):
                try:
                    name = boxscore[home_away]['players']['ID'+str(pitcher_list[i])]['person']['fullName']
                    inningsPitched = boxscore[home_away]['players']['ID'+str(pitcher_list[i])]['stats']['pitching']['inningsPitched']
                    hits = boxscore[home_away]['players']['ID'+str(pitcher_list[i])]['stats']['pitching']['hits']
                    earnedRuns = boxscore[home_away]['players']['ID'+str(pitcher_list[i])]['stats']['pitching']['earnedRuns']
                    baseOnBalls = boxscore[home_away]['players']['ID'+str(pitcher_list[i])]['stats']['pitching']['baseOnBalls']
                    strikeOuts = boxscore[home_away]['players']['ID'+str(pitcher_list[i])]['stats']['pitching']['strikeOuts']
                    numberOfPitches = boxscore[home_away]['players']['ID'+str(pitcher_list[i])]['stats']['pitching']['numberOfPitches']
                    era = boxscore[home_away]['players']['ID'+str(pitcher_list[i])]['seasonStats']['pitching']['era']
                    pitching_df.loc[i] = [name, inningsPitched, hits, earnedRuns, baseOnBalls, strikeOuts, numberOfPitches, era]
                except:
                    pass
            pitching_df = pitching_df.set_index("투수명")
            return pitching_df
        
        tab1, tab2 = st.tabs([away_h, home_h])
        with tab1:
            st.write(batting_stats('away'))
            st.write(pitching_stats('away'))
        
        with tab2:
            st.write(batting_stats('home'))
            st.write(pitching_stats('home'))
    except:
        st.title('금일 경기가 없습니다.')