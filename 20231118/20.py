import requests
from bs4 import BeautifulSoup

#local = input('지역명 입력:')
url = 'https://finance.naver.com/item/main.naver?code='


response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#chart_area > div.rate_info > div > p.no_today')
    #print(title)
    print(title.get_text())
elif response.status_code == 404:
    print('그딴 페이지를 찾을수 없어')

else :
    print(response.status_code)
