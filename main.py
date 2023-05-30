import Keyword_Analisys as ka
import pandas as pd
import numpy as np

import folium
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ka.get_Keyword_Analisys()

# 각 파일 불러오기
nuptiality = pd.read_csv('혼인율.csv')
birthrate = pd.read_csv('출산율.csv')
apart_trade = pd.read_csv('주택매매가격.csv')
apart_lease = pd.read_csv('주택전세가격.csv')
job_get_loss = pd.read_csv('취업,실업률.csv',skiprows=[0,1]) # skiprows -> 맨 위의 필요없는 행 삭제
houseMember_rate = pd.read_csv('가구구성 변화율.csv',skiprows=[0,1,2])


# 데이터 전처리
# 혼인율 파일
# 필요없는 행 삭제
for i in range(2,4):
    nuptiality = nuptiality.drop(index=i,axis=0)

#열 이름 변경 및 index를 항목으로 변경 / index 이름 변경
nuptiality = nuptiality.rename(columns={'Unnamed: 0' : '항목'})
nuptiality = nuptiality.set_index('항목')
nuptiality = nuptiality.set_index(pd.Index(['조혼인율','혼인건수']))

# 출산율 파일
# 필요없는 행 삭제
for i in range(1,4):
    birthrate = birthrate.drop(index=i,axis=0)
    
# 열 이름을 항목으로 변경 / index를 항목으로 변경
birthrate = birthrate.rename(columns={'Unnamed: 0': '항목'})
birthrate = birthrate.set_index('항목')

# 주택매매가격 파일
#열 이름을  지역으로 변경 / index를 지역으로 변경
apart_trade = apart_trade.rename(columns={'Unnamed: 0' : '지역'})
apart_trade = apart_trade.set_index('지역')


# 주택전세가격 파일
# 열 이름을  지역으로 변경 / index를 지역으로 변경
apart_lease = apart_lease.rename(columns={'Unnamed: 0' : '지역'})
apart_lease = apart_lease.set_index('지역')


# 취업/실업률 파일
# 필요없는 행 삭제
for i in range(8,13):
    job_get_loss = job_get_loss.drop(index=i,axis=0)
    
# 열 이름 변경
job_get_loss = job_get_loss.rename(columns={'Unnamed: 0' : '항목'})

# index를 항목으로 변경 / index 이름 재 설정
job_get_loss = job_get_loss.set_index('항목')
job_get_loss = job_get_loss.set_index(pd.Index(['취업자 증감','농립어업','제조업','건설업','실업자','실업률(%)','청년실업자','청년실업률(%)']))


# 가구구성원 파일
# 필요없는 행 삭제
for i in range(7,12):
    houseMember_rate = houseMember_rate.drop(index=i,axis=0)

# 열 이름 변경 / index를 년도로 변경
houseMember_rate = houseMember_rate.rename(columns={'Unnamed: 0' : '년도', 'Unnamed: 1' : '가구수(천 단위)','Unnamed: 8' : '평균 가구원수'})
houseMember_rate = houseMember_rate.set_index('년도')

# 행 <-> 열 바꿔주기 (년도를 열로 변경)
houseMember_rate = houseMember_rate.transpose()











