import re
import urllib
from urllib import request


url = 'https://movie.douban.com/top250'

'''sometimes we need proxy to access internet

proxies = {"http": "http://ys1003:UTdba@12@sdcwsa01.commscope.com:80"}
proxy_support = request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
'''

data = request.urlopen(url).read()
data = data.decode('UTF-8')
# set an object of regular expression
info_pattern = re.compile('<span class="title">')
for x in info_pattern.findall(data):
    print(x)




