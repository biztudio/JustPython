import re
import requests
from bs4 import BeautifulSoup


class StockListFromEastMoney:
    def __init__(self):
        self.stock_list_site = 'http://quote.eastmoney.com/stocklist.html'
        self.stock_main_site = 'http://stock.eastmoney.com/'

    def find_stock_link_items(self, tag):
        if tag.name != 'a' or not tag.has_attr('href'):
            return False
        # Stock codes list in Shanghai start with 6, while 0 for Shenzhen counterpart
        link_pattern = re.compile('http://quote.eastmoney.com/s[h,z][0,6]\d+.html', re.IGNORECASE)
        return tag.name == 'a' and tag.has_attr('target') and re.match(link_pattern, tag['href'])

    def fetch_stock_list(self):
        response = requests.get(self.stock_list_site)
        if response.encoding == 'ISO-8859-1':
            response.encoding = 'GBK'
        content = response.text
        return [(stock['href'][-11:-5], stock.text, stock['href']) for stock in BeautifulSoup(content, 'html.parser').find_all(self.find_stock_link_items)]


if __name__ == '__main__':
    fetch = StockListFromEastMoney()
    stock_list = fetch.fetch_stock_list()
    print(stock_list)

# requests 中文乱码
# http://www.zhetenga.com/view/python%E7%9A%84requests%E7%B1%BB%E6%8A%93%E5%8F%96%E4%B8%AD%E6%96%87%E9%A1%B5%E9%9D%A2%E5%87%BA%E7%8E%B0%E4%B9%B1%E7%A0%81-0abbaa140.html
# http://jingyan.baidu.com/article/2c8c281dbb969d0008252a80.html