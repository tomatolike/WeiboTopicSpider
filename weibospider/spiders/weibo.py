# -*- coding: utf-8 -*-
import scrapy
from weibospider.items import BaseinfoItem,Fans_listItem,Topic_postItem,Comment_listItem
from selenium import webdriver
import time
import random

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
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
    	self.cookie = "SINAGLOBAL=6682242679096.176.1508122383526; UM_distinctid=1601673940f681-01532d4f31f69d-17396d57-1aeaa0-160167394118cd; un=18867158066; UOR=www.ali213.net,widget.weibo.com,login.sina.com.cn; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFWF7E16egjecUNI.cWZTZr5JpX5KMhUgL.Fo-4e0-0SKnXeh-2dJLoIXnLxKBLB.zL122LxK-LBKBLBK.LxKBLB.zLB.BLxKML1-2L1hBLxKqL1-eLBKnLxK-LB-BL1K5LxKML12-L12zLxK-L12qLB-qt; ALF=1546048915; SSOLoginState=1514512916; SCF=AgwbdQ3uYn_4CQM-iwkVmGqig7g6I5Y7ZxG5mWQ-PHEFQTXeRuSgXKB79xtz7lCe3ZXbFkYLIJ7_EEhsrcZHNeg.; SUB=_2A253QdJEDeRhGeNH6FcS9SbIyzmIHXVUN0SMrDV8PUNbmtBeLUbAkW9NStbCZX9q68seqe75D2rWrIqWc-dr4XA8; SUHB=0auAk0xyYuzJnC; _s_tentry=login.sina.com.cn; Apache=693521043815.8701.1514512919866; ULV=1514512919918:16:11:8:693521043815.8701.1514512919866:1514477518108; YF-Page-G0=00acf392ca0910c1098d285f7eb74a11"


    def start_requests(self):
    	start_urls = 'https://d.weibo.com/100803?from=page_huati_tab'
    	req = scrapy.Request(url=start_urls,callback=self.parse,errback=self.errback)
    	req.meta['useragent']=random.choice(self.agent)
    	req.meta['cookie']=self.cookie
    	req.meta['name']="话题榜首页"
    	req.meta['time']='1'
    	req.meta['page']=-1
    	req.meta['count']=-1
    	req.meta['t_id']=""
    	yield req

    def parse4(self, response):
    	print("4")

    def parse(self, response):
    	print("开始处理话题榜")
    	lis = response.xpath("//div[@class='text_box']")
    	#print(response.body)
    	print(len(lis))
    	if(len(lis)==0):
    		req2 = scrapy.Request(url=response.url,callback=self.parse,errback=self.errback,dont_filter = True)
    		req2.meta['useragent']=random.choice(self.agent)
    		req2.meta['cookie']=self.cookie
    		req2.meta['name']=response.meta['name']
    		req2.meta['time']='1'
    		req2.meta['page']=-1
    		req2.meta['count']=-1
    		req2.meta['t_id']=""
    		yield req2
    	else:
    		for i,li in enumerate(lis):
    			if(i==1):
    				break
    			title = li.xpath(".//a[@target='_blank']/text()").extract()[0]
    			title = title.replace(" ","")
    			title = title.replace("\t","")
    			title = title.replace("\n","")
    			#print("name="+title)
    			url = li.xpath(".//a[@target='_blank']/@href").extract()[0]
    			#print(url)
    			req = scrapy.Request(url="https:"+url,callback=self.parse2,errback=self.errback)
    			req.meta['useragent']=random.choice(self.agent)
    			req.meta['cookie']=self.cookie
    			req.meta['name']=title
    			req.meta['time']='2'
    			req.meta['page']=-1
    			req.meta['count']=-1
    			req.meta['t_id']=""
    			yield req

    def parse2(self, response):
    	net = response.xpath("//a[@class='WB_cardmore WB_cardmore_noborder S_txt1 clearfix']/@href")
    	print(len(net))
    	if(len(net)==0):
    		print("wrong!")
    		req2 = scrapy.Request(url=response.url,callback=self.parse2,errback=self.errback,dont_filter = True)
    		req2.meta['useragent']=random.choice(self.agent)
    		req2.meta['cookie']=self.cookie
    		req2.meta['name']=response.meta['name']
    		req2.meta['time']='2'
    		req2.meta['page']=-1
    		req2.meta['count']=-1
    		req2.meta['t_id']=""
    		yield req2
    	else:
    		net = response.xpath("//a[@class='WB_cardmore WB_cardmore_noborder S_txt1 clearfix']/@href").extract()[0]
    		print(net)
    		req = scrapy.Request(url=net,callback=self.parse3,errback=self.errback)
    		url = net
    		req.meta['useragent']=random.choice(self.agent)
    		req.meta['cookie']=self.cookie
    		req.meta['name']=response.meta['name']
    		req.meta['time']='3'
    		req.meta['page']=1
    		req.meta['count']=0
    		req.meta['t_id']=url[url.find("/p/")+3:url.find("/em")]
    		yield req

    def parse3(self, response):
    	ti = response.xpath("//h1[@class='username']")
    	if(len(ti)==0):
    		print(response.meta['name']+"读取失败，重新读取")
    		req2 = scrapy.Request(url=response.url,callback=self.parse3,errback=self.errback,dont_filter = True)
    		req2.meta['useragent']=random.choice(self.agent)
    		req2.meta['cookie']=self.cookie
    		req2.meta['name']=response.meta['name']
    		req2.meta['time']='3'
    		req2.meta['page']=1
    		req2.meta['count']=0
    		req2.meta['t_id']=response.meta['t_id']
    		yield req2
    	else:
    		if(response.meta['time']=='3'):
	    		title = response.xpath("//h1[@class='username']/text()").extract()[0]
	    		print("title="+title)
	    		oldurl = response.url
	    		t_id = oldurl[oldurl.find("/p/")+3:oldurl.find("/em")]
	    		print("t_id="+t_id)
	    		para = response.xpath("//table[@class='tb_counter']/tbody/tr/td")
	    		read_c=""
	    		dic_c=""
	    		fans_c=""
	    		#print(para)
	    		for i,p in enumerate(para):
	    			np = p.xpath(".//strong/text()").extract()[0]
	    			np = np.replace(" ","")
	    			np = np.replace("\t","")
	    			np = np.replace("\n","")
	    			if(i==0):
	    				read_c = np
	    				print("read_c="+read_c)
	    			elif(i==1):
	    				dic_c = np
	    				print("dic_c="+dic_c)
	    			elif(i==2):
	    				fans_c = np
	    				print("fans_c="+fans_c)
	    			else:
	    				print("不知道的属性")
	    		host = response.xpath("//div[@class='title W_fb W_autocut ']/a")
	    		host_n = host[0].xpath("./@title").extract()[0]
	    		print("host_name="+host_n)
	    		host_id = host[0].xpath("./@usercard").extract()[0]
	    		host_id = host_id[host_id.find("id=")+3:host_id.find("&type")]
	    		print("host_id="+host_id)
	    		con = response.xpath("//div[@id='Pl_Third_Inline__3']/div/div/div")
	    		print(con)
	    		content = ""
	    		if(len(con)==0):
	    			print("没有话题导语")
	    		else:
	    			print("有导语：",end="")
	    			content = con.xpath("string(.)").extract()[0]
	    			content = content.replace("\t","")
	    			content = content.replace("\n","")
	    			print(content)
	    		fans_url = response.xpath("//a[@class='t_link S_txt1']/@href").extract()[0]
	    		print("fans_url="+fans_url)
	    		freq = scrapy.Request(url="https:"+fans_url,callback=self.parse4,errback=self.errback)
	    		freq.meta['useragent']=random.choice(self.agent)
	    		freq.meta['cookie']=self.cookie
	    		freq.meta['name']=response.meta['name']
	    		freq.meta['time']='5'
	    		freq.meta['page']=1
	    		freq.meta['count']=0
	    		freq.meta['t_id']=t_id
	    		#yield freq

	    	tps = response.xpath("//div[@class='WB_cardwrap WB_feed_type S_bg2 WB_feed_like']")
	    	tps2 = response.xpath("//div[@class='WB_cardwrap WB_feed_type S_bg2 WB_feed_vipcover WB_feed_like']")
	    	print("tps=",len(tps))
	    	print("tps2=",len(tps2))
	    	tps = tps+tps2
	    	print("tps=",len(tps))
	    	for i,tp in enumerate(tps):
	    		u_id = tp.xpath("./@tbinfo").extract()[0]
	    		u_id = u_id.replace("\n","")
	    		print("u_id="+u_id+"\t",end="")
	    		u_name = tp.xpath(".//a[@class='W_f14 W_fb S_txt1']/@title").extract()[0]
	    		u_name = u_name.replace("\n","")
	    		print("u_name="+u_name+"\t",end="")
	    		tp_id = tp.xpath("./@mid").extract()[0]
	    		tp_id = tp_id.replace("\n","")
	    		print("tp_id="+tp_id+"\t",end="")
	    		time = tp.xpath(".//a[@node-type='feed_list_item_date']/@title").extract()[0]
	    		time = time.replace("\n","")
	    		print("time="+time+"\t",end="")
	    		frs = tp.xpath(".//div[@class='WB_from S_txt2']/a")
	    		#print(frs)
	    		if(len(frs)==0 or len(frs)==1):
	    			fr = "没有来源"
	    		else:
	    			fr = frs[1].xpath("string(.)").extract()[0]
	    			fr = fr.replace("\n","")
	    		print("fr="+fr+"\t")
	    	#判断有无下一页或者是否达到五百条
	    	nextpages = response.xpath("//a[@class='page next S_txt1 S_line1']/@href")
	    	if(len(nextpages)==0):
	    		print("没有下一页了")
	    	else:
	    		response.meta['count']=response.meta['count']+len(tps)
	    		if(response.meta['count']>=50):
	    			print(response.meta['name']+"已经五百条了")
	    		else:
	    			nextpage=response.xpath("//a[@class='page next S_txt1 S_line1']/@href").extract()[0]
	    			nextpage="https://weibo.com"+nextpage
	    			req = scrapy.Request(url=nextpage,callback=self.parse3,errback=self.errback)
	    			req.meta['useragent']=random.choice(self.agent)
	    			req.meta['cookie']=self.cookie
	    			req.meta['name']=response.meta['name']
	    			req.meta['time']='4'
	    			req.meta['page']=response.meta['page']+1
	    			req.meta['count']=response.meta['count']
	    			req.meta['t_id']=t_id
	    			yield req
			

    		

    '''	
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

	'''    	



    def errback(self, failure):
    	print(failure)