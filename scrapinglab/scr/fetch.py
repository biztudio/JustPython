import re
import urllib
from urllib import request
import play_env_setting


url = 'https://movie.douban.com/top250'

proxyinfo = play_env_setting.ProxySetting()
opener = urllib.request.build_opener(proxyinfo.get_proxy_for_urllib())
# install the openen on the module-level
urllib.request.install_opener(opener)

info_pattern = re.compile('"title">\w*<')
with request.urlopen(url) as response:
    data = response.read().decode('UTF-8')
    for x in info_pattern.findall(data):
        print(x)
