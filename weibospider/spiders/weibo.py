# -*- coding: utf-8 -*-
import scrapy
from weibospider.items import BaseinfoItem,Fans_listItem,Topic_postItem,Comment_listItem
from selenium import webdriver
import time
import random

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['http://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6']
    success=0

    def __init__(self):
    	self.success=0
    	self.agent=self.user_agent=[
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]

    def parse(self, response):
    	print("热搜榜爬取结束")
    	title = response.xpath("//tbody/tr")
    	for i,t in enumerate(title):
    		if i == 20:
    			break
    		name = t.xpath("./td[@class='td_02']//a/text()").extract()[0]
    		#print("name="+name)
    		#print(name)
    		length = name.find("...")
    		if(length!=-1):
    			name=name[0:length]
    		name=name.replace(' ','')
    		print(name)
    		url = t.xpath("./td[@class='td_02']//a/@href").extract()[0]
    		url = "http://s.weibo.com"+url
    		req = scrapy.Request(url, callback=self.parse2)
    		req.meta['name']=name
    		req.headers['User_Agent']=random.choice(self.agent)
    		yield req

    def parse2(self, response):
    	print("success=",self.success)
    	if(self.success<10):
    		on = response.meta['name']
    		#print(on)
    		topic = response.xpath("//p[@class='comment_txt']")
    		#print("len=",len(topic))
    		for i,t in enumerate(topic):
    			#print("i=",i)
    			name = t.xpath("./a[@class='a_topic W_linkb']/em/text()")
    			if(len(name)==0):
    				continue
    			name = t.xpath("./a[@class='a_topic W_linkb']/em/text()").extract()[0]
    			name=name.replace(' ','')
    			#print(name)
    			#print(name.find(on))
    			if(name.find(on)==-1):
    				continue
    			url = t.xpath("./a[@class='a_topic W_linkb']/@href").extract()[0]
    			print(name)
    			print(url)
    			self.success=self.success+1
    			print("二级搜索已完成",self.success)
    			url = "http:"+url
    			req=scrapy.Request(url,callback=self.parse3)
    			req.meta['name']=name
    			req.headers['User_Agent']=random.choice(self.agent)
    			yield req
    			break

    def parse3(self, response):
    	print(response.meta['name'])
    	title = response.xpath("//dev[@class='pf_username clearfix']/h1/text()")
    	if(len(title)==0):
    		print("没有title，出错了")
    	else:
    		title= response.xpath("//dev[@class='pf_username clearfix']/h1/text()").extract()[0]
    	print("title="+title)
    	
    	fans_url = response.xpath("//a[@class='t_link S_txt1']/@href")
    	if(len(fans_url)==0):
    		print("没有fans，出错了")
    	else:
    		fans_url = response.xpath("//a[@class='t_link S_txt1']/@href").extract()[0]
    	print("fans_url="+fans_url)
    	
    	t_id = fans_url[(fans_url.find("/p/")+3):(fans_url.find("/followlist"))]
    	print("t_id="+t_id)
    	
    	fans_c = response.xpath("//a[@class='t_link S_txt1']/strong/text()")
    	if(len(fans_c==0)):
    		print("没有fans数量，出错了")
    	else:	
    		fans_c = response.xpath("//a[@class='t_link S_txt1']/strong/text()").extract()[0]
    	print("fans_c="+fans_c)

    	



    def errback(self, failure):
    	print(failure)