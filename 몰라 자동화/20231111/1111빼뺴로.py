import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/webhp?hl=ko&sa=X&ved=0ahUKEwi_ybfQwsyCAxVW0TQHHfB9Ga4QPAgJ'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#now > div > div.location_info_area > div.location_area > strong')
    print(soup)
elif response.status_code == 404:
    print('그딴 페이지를 찾을수 없어')

else :
    print(response.status_code)


#

