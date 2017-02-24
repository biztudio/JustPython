import requests
from bs4 import BeautifulSoup
import play_env_setting


url = 'https://movie.douban.com/top250'
proxyinfo = play_env_setting.ProxySetting()
response = requests.get(url, proxies = proxyinfo.proxymap)
soup = BeautifulSoup(response.text, 'html.parser')
for div_movie in soup.find_all('div', {'class':'info'}):
    print(div_movie.find('span', {'class':'title'}).text + ' 得分: '+ div_movie.find('span', {'class':'rating_num'}).text)