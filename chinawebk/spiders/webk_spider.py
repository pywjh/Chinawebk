# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy_redis.spiders import RedisSpider
from ..items import ChinawebkItem


class WebkSpiderSpider(RedisSpider):
    name = 'webk_spider'
    # allowed_domains = ['99114.com']
    # start_urls = ['http://www.99114.com/']
    redis_key = 'chinawebk:urls'

    def parse(self, response):
        '''获取大范围的搜索链接'''
        goods_list = response.xpath('//li[@class="fd-clr"]/a/@href').extract()
        for thing in goods_list:
            yield scrapy.Request(url=thing, callback=self.detial_list)

    def detial_list(self, response):
        '''获取搜索到的(有图片)商品主链接'''

        # 翻页
        next_page = response.xpath('//a[@class="J_Ajax num icon-tag"]/@href').extract_first()
        url = 'http://gongying.99114.com%s'%next_page
        yield scrapy.Request(url=url, callback=self.detial_list)

        detial_info_list = response.xpath('//div[@class="pic-box-inner"]/div//a/@href').extract()
        for detial_info in detial_info_list:
            yield scrapy.Request(url=detial_info, callback=self.detial_info)

    def detial_info(self, response):
        '''获取(详细)商品信息'''
        items = ChinawebkItem()

        goods_store_title =  response.xpath('//p[@class="logo-cname-p clearfix"]/a/text()').extract_first().strip()
        store_href = response.xpath('//p[@class="logo-cname-p clearfix"]/a/@href').extract_first()
        goods_title = response.xpath('//h1/text()').extract_first().strip()
        goods_attrs = '-'.join(response.xpath('string(//table[@class="table-introduce"])').re('\w+'))
        price = ''.join(response.xpath('string(//tbody[@id="number-price"])').re('[\S\w+]'))
        delivery_place = response.xpath('//span[@class="areaname"]/text()').extract_first().strip()
        seller_name = ''.join(response.xpath('string(//div[@class="contxt"]/p)').re('\w+'))
        seller_TEL = response.xpath('//span[@class="phoneNumber"]/text()').extract_first()

        if goods_store_title:
            items['goods_store_title'] = goods_store_title
        if store_href:
            items['store_href'] = store_href
        if goods_title:
            items['goods_title'] = goods_title
        if goods_attrs:
            items['goods_attrs'] = goods_attrs
        if price:
            items['price'] = price
        if delivery_place:
            items['delivery_place'] = delivery_place
        if seller_name:
            items['seller_name'] = seller_name
        if seller_TEL:
            items['seller_TEL'] = seller_TEL

        yield items
