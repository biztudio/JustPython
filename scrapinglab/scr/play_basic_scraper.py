import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban_movie_spider'
    start_urls = ['https://movie.douban.com/top250']
