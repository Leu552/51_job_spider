# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from . import settings
class WyjobPipeline(object):
    def __init__(self, ):
        self.conn = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            use_unicode=False)
        self.cursor = self.conn.cursor()

    # pipeline 默认调用
    def process_item(self, item, spider):
        # 调用插入数据的方法
        self.insertData(item)
        return item
 # 插入数据方法
    def insertData(self, item):
        sql = "insert into wyjob_php(job, company, place, salary) VALUES(%s, %s, %s, %s);"
        params = (item['job'], item['company'], '杭州', item['salary'])
        self.cursor.execute(sql, params)
        self.conn.commit()