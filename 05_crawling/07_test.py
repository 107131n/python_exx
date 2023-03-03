from urllib import request
import requests
from bs4 import BeautifulSoup
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB=%B4%84
key = input('검색어 >>> ')
url = 'https://search.naver.com/search.naver'
param = {
    'query':key,
    'where':'image'
}
res = requests.get(url,params=param)
soup =BeautifulSoup(res.text,'lxml')
result = soup.find_all('img')
print(result)
for i, item in enumerate(result):
    try:
        print(item['src'])
        index = item['src'].index('&') #없으면 오류, find는 -1 반환 
        src =item['src'][:index]
        print('--------')
        print(src)
        filetype = src[-3:]
        print(filetype)
        request.urlretrieve(src, '05_crawling/down/'+str(i)+'.'+filetype)
    except:
        print('url 오류')
    if i >= 10:break
