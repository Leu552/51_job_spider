# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WyjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 工作名称
    job = scrapy.Field()
    # 公司名称
    company = scrapy.Field()
    # 工作地点
    place = scrapy.Field()
    # 工作薪资
    salary = scrapy.Field()

    pass
