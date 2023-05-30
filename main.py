import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import array
import folium
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from collections import Counter
from konlpy.tag import Okt
from wordcloud import WordCloud
import os
os.environ['JAVA_HOME'] = os.path.expanduser('C:\Program Files\Java\jdk-20')

# 네이버에 혼인율 검색 후 10 페이지까지 뉴스 제목 스크래핑
list = []

for i in range(1, 100, 10):
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query=혼인율&start={i}")
    soup = BeautifulSoup(response.text,'html.parser')

    links = soup.select('.news_tit')

    for link in links:
        title = link.text
        # url = link.attrs['href'] 뉴스 주소 따오기는 생략
        list.append([title])


# 스크래핑 한 내용 csv 파일로 저장
# 처음에는 아래 내용 주석 풀고 Run 하기~
# f = open('혼인율_Newslist.txt','w',encoding='utf-8' ,newline='')
# list = str(list)
#
# for i in list:
#     f.write(i)
#     if i ==']':
#         f.write('\n')
# f.close()

#키워드 분석 시작
with open('혼인율_Newslist.txt', 'r', encoding='utf-8') as d:
    text = d.read()

okt = Okt()
output = okt.pos(text) #형태소와 품사 추출

words = []
# 형용사와 명사만 리스트에 넣어주기
for i, j in output:
    if j in['Noun','Adjective']:
        words.append(i)

#제외 할 단어 추가
stop_words = "또 명 세 의 혼인 혼인율 율 과 더 악 그 률 전 길 별 인 더 안 해도 점 용 시 때 브 새 뚝 수 제 탓 순 간 최 돌 줄 게 사 로 늘 것 무 치 실 나선 낮아 중"
stop_words = set(stop_words.split(' '))
#불용어 제외
words = [i for i in words if not i in stop_words]
#가장 많이 나온 단어 100개 저장
count = Counter(words)
count = count.most_common(100)

# 키워드 분석 시각화
mask = Image.new("RGBA",(2500,2200),(255,255,255))
image = Image.open('C:/Users/Lovers2019/PycharmProjects/pythonProject/heart.png').convert('RGBA')
x,y = image.size
mask.paste(image,(0,0,x,y),image)
mask = np.array(mask)

# 폰트 지정
font = 'C:/Windows/Fonts/맑은고딕/malgun.ttf'
word_cloud = WordCloud(font_path=font, background_color='black',max_font_size=400,mask=mask, colormap='prism').generate_from_frequencies(dict(count))
plt.figure(figsize=(10,8))
plt.imshow(word_cloud)
plt.axis('off')
plt.savefig('혼인율.png',bbox_inches='tight')
plt.show()

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











