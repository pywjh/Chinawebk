# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy import Field


class ChinawebkItem(scrapy.Item):
    # 店铺名
    goods_store_title = Field()
    # 商品名
    goods_title = Field()
    # 商品参数
    goods_attrs = Field()
    # 价格
    price = Field()
    # 发货处
    delivery_place = Field()

    # 卖家
    seller_name = Field()
    # 电话
    seller_TEL = Field()
    # 店铺网址
    store_href = Field()



