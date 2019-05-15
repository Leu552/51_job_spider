# coding=utf-8
# -*- coding: utf-8 -*-

import scrapy
import requests
from ..items import WyjobItem


class WyjobSpider(scrapy.Spider):
    # name是spider最重要的属性, 它必须被定义。同时它也必须保持唯一
    name = 'wyjob'
    start_urls = []
    # 给start_urls加入不同页面的地址
    for i in range(1,15):
        start_urls.append('https://search.51job.com/list/040000,000000,0000,00,9,99,PHP%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,'+str(i)+'.html')
    # 可选定义。包含了spider允许爬取的域名(domain)列表(list)
    allowed_domains = ['search.51job.com']
    # bash_url = 'https://search.51job.com/list/050000,000000,0000,00,9,99,PHP,2,'
    # bashurl = '.html'

    # def start_requests(self):
    #     for i in range(1, 4):
    #         url = self.bash_url + str(i) + self.bashurl
    #
    #         yield scrapy.Request(url, self.parse)

    # response是根据start_urls请求的结果，也可以用start_requests自己编写
    def parse(self,response):
        joblist = response.xpath("//div[@class='dw_table']/div[@class='el']")
        for i in joblist:
            # 理解成实例化吧
            item = WyjobItem()
            # 记得要加 . 表示从当前节点
            # [0]是拿取第一个列表内容文本，如果没有则会拿到一个列表
            item['job'] = i.xpath('./p/span/a/@title')[0].extract()
            item['company'] = i.xpath('./span/a/@title')[0].extract()
            item['place'] = i.xpath("./span[@class='t3']/text()")[0].extract()
            item['salary'] = i.xpath("./span[@class='t4']/text()")[0].extract()
            print('++++++++++++++++++++++++++++++++++++++内容start++++++++++++++++++++++++++++++++++++++++++++++')
            print(item)
            print('++++++++++++++++++++++++++++++++++++++内容end++++++++++++++++++++++++++++++++++++++++++++++')
            yield item

