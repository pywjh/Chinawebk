# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .settings import MONGO_DB_HOST, MONGO_DB_PORT

class ChinawebkPipeline(object):

    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(
            host=MONGO_DB_HOST,
            port=MONGO_DB_PORT,
        )
        self.db = self.conn['tanzhou_homework']
        self.connection = self.db['chinawebk']

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.connection.insert(dict(item))
        # print(item)
        return item
