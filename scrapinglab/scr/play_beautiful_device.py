import re
import requests
from bs4 import BeautifulSoup
import play_env_setting
import play_beautiful_device_filter

#Test 1, fetch Cisco card N9508
filter = play_beautiful_device_filter.BeautifulFilter()
url = filter.CiscoFilter['URL']['Nexus9508']
proxyinfo = play_env_setting.ProxySetting()
response = requests.get(url, proxies = proxyinfo.proxymap)
card_table = BeautifulSoup(response.text, 'html.parser').find_all('tr', {'valign':'top', 'align':'left'})
for card_row in card_table:
    card_name = card_row.find_all('p', {'class':'pChart_subheadCMT'})
    card_detail = card_row.find_all('p', {'class':'pChart_bodyCMT'})
    if card_name and card_detail and re.search('card', card_detail[0].text):
        print(card_name[0].text + ': ' + card_detail[0].text)
