import re
import urllib
from urllib import request


url = 'https://movie.douban.com/top250'

'''sometimes we need proxy to access internet
proxy = request.ProxyHandler({'http': 'biztudio.github.io:80'})
opener = request.build_opener(proxy)
request.install_opener(opener)
'''

data = request.urlopen(url).read()
data = data.decode('UTF-8')
# set an object of regular expression
info_pattern = re.compile('<span class="title">\w*</span>')
for x in info_pattern.findall(data):
    print(x)




