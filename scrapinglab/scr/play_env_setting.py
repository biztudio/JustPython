#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''to get proxy '''
import urllib


class ProxySetting:
    '''proxy setting info'''
    def __init__(self):
        self.proxymap = {"http": "http://ys1003:UTdba@12@sdcwsa01.commscope.com:80",
                         "https": "http://ys1003:UTdba@12@sdcwsa01.commscope.com:80"}


    def get_proxy_for_urllib(self):
        '''return the proxy setting to access internet'''
        return urllib.request.ProxyHandler(self.proxymap)
        