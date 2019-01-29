# Chinawebk
scrapy to crawl the data

本项目是利用scrapy_redis分布式框架来爬取网站中国网库，爬取商品的重要信息，并将数据保存在Mongo_db中。
为了避免反爬，使用了之前项目的代理池(middlewares.py)，代理池的接口是利用flask启动的一个web服务进行使用。
