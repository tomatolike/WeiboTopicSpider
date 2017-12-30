# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    t_id = scrapy.Field()
    name = scrapy.Field()
    read_c = scrapy.Field()
    dis_c = scrapy.Field()
    fans_c = scrapy.Field()
    host_n = scrapy.Field()
    host_id = scrapy.Field()
    content = scrapy.Field()

class Fans_listItem(scrapy.Item):
	t_id = scrapy.Field()
	u_name = scrapy.Field()
	u_id = scrapy.Field()
	rank_n = scrapy.Field()

class Topic_postItem(scrapy.Item):
	t_id = scrapy.Field()
	tp_id = scrapy.Field()
	u_name = scrapy.Field()
	u_id = scrapy.Field()
	time = scrapy.Field()
	fr = scrapy.Field()
	comment_c = scrapy.Field()
	trans_c = scrapy.Field()
	zan_c = scrapy.Field()
	zhuan_id = scrapy.Field()
	content = scrapy.Field()

class Comment_listItem(scrapy.Item):
	tp_id = scrapy.Field()
	comment_id = scrapy.Field()
	u_id = scrapy.Field()
	u_name = scrapy.Field()
	content = scrapy.Field()
    



