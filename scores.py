import streamlit as st
import pandas as pd
import statsapi
from datetime import datetime

def run_scores():
    # today = datetime.today().strftime("%m/%d/%Y")

    sched = statsapi.schedule(start_date='10/02/2022',team=143)
    date = st.sidebar.date_input('날짜 선택')
    date = date.strftime("%m/%d/%Y")
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
        team_id = 1113
    elif team == '워키 브루어스':
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
