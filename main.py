import numpy as np
import pandas as pd
import array
import folium
import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud

nuptiality = pd.read_csv('혼인율.csv')
birthrate = pd.read_csv('출산율.csv')
apart_trade = pd.read_csv('주택매매가격.csv')
apart_lease = pd.read_csv('주택전세가격.csv')
job_get_loss = pd.read_csv('취업,실업률.csv',skiprows=[0,1]) # skiprows -> 맨 위의 필요없는 행 삭제
houseMember_rate = pd.read_csv('가구구성 변화율.csv',skiprows=[0,1,2])

# 필요없는 행 삭제 index 8 ~ 12
for i in range(8,13):
    job_get_loss = job_get_loss.drop(index=i,axis=0)

# 열 이름 안들어가 있는 것들 넣어주기
job_get_loss = job_get_loss.rename(columns={'Unnamed: 0' : '항목'})


# 필요없는 행 삭제 index 8 ~ 12
for i in range(7,12):
    houseMember_rate = houseMember_rate.drop(index=i,axis=0)

# 열 이름 안들어가 있는 것들 넣어주기
houseMember_rate = houseMember_rate.rename(columns={'Unnamed: 0' : '년도', 'Unnamed: 1' : '가구수(천 단위)','Unnamed: 8' : '평균 가구원수'})








