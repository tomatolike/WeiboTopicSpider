# -*- coding: utf-8 -*-
import scrapy
from weibospider.items import BaseinfoItem,Fans_listItem,Topic_postItem,Comment_listItem
from selenium import webdriver
import time
import random

class WeiboSpider(scrapy.Spider):
	name = 'weibo'
	allowed_domains = ['weibo.com','weibo.cn']
	success=0

	def __init__(self):
		self.success=0
		self.tlist=[]
		self.tplist=[]
		self.userlist=[]
		self.clist=[]
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
		self.cookie = "SINAGLOBAL=6682242679096.176.1508122383526; UM_distinctid=1601673940f681-01532d4f31f69d-17396d57-1aeaa0-160167394118cd; UOR=www.ali213.net,widget.weibo.com,login.sina.com.cn; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; _s_tentry=-; Apache=8829399666547.459.1514741582973; ULV=1514741582982:18:1:2:8829399666547.459.1514741582973:1514694990806; YF-V5-G0=2a21d421b35f7075ad5265885eabb1e4; YF-Page-G0=280e58c5ca896750f16dcc47ceb234ed; login_sid_t=7ff750e5636caccf913c272fefec1d0a; cross_origin_proto=SSL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFWF7E16egjecUNI.cWZTZr5JpX5K2hUgL.Fo-4e0-0SKnXeh-2dJLoIXnLxKBLB.zL122LxK-LBKBLBK.LxKBLB.zLB.BLxKML1-2L1hBLxKqL1-eLBKnLxK-LB-BL1K5LxKML12-L12zLxK-L12qLB-qt; ALF=1546277610; SSOLoginState=1514741611; SCF=AgwbdQ3uYn_4CQM-iwkVmGqig7g6I5Y7ZxG5mWQ-PHEFs2LA8sy3E8gOtRe9Sjk4XHPsv4ttW9do-Jf-1wiWzHU.; SUB=_2A253TW87DeRhGeNH6FcS9SbIyzmIHXVUO8fzrDV8PUNbmtBeLW_CkW9NStbCZWmS5-9XWfLAEredU06j5NHKEP1q; SUHB=00xpL3_snuYj0r; un=18867158066; wvr=6; wb_cusLike_5935358405=N"


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
				if(i==10):
					break
				title = li.xpath(".//a[@target='_blank']/text()").extract()[0]
				title = title.replace(" ","")
				title = title.replace("\t","")
				title = title.replace("\n","")
				print("name="+title)
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
			print(response.meta['name']+"wrong!")
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
			print(response.meta['name']+":"+net)
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
		t_id = response.meta['t_id']
		if(len(ti)==0):
			print(response.meta['name']+"读取失败，重新读取")
			req2 = scrapy.Request(url=response.url,callback=self.parse3,errback=self.errback,dont_filter = True)
			req2.meta['useragent']=random.choice(self.agent)
			req2.meta['cookie']=self.cookie
			req2.meta['name']=response.meta['name']
			req2.meta['time']=response.meta['time']
			req2.meta['page']=response.meta['page']
			req2.meta['count']=response.meta['count']
			req2.meta['t_id']=response.meta['t_id']
			yield req2
		else:
			if(response.meta['time']=='3'):
				newtopic = BaseinfoItem()
				title = response.xpath("//h1[@class='username']/text()").extract()[0]
				self.tlist.append(title)
				newtopic['name'] = title
				print("title="+title)
				oldurl = response.url
				t_id = oldurl[oldurl.find("/p/")+3:oldurl.find("/em")]
				newtopic['t_id'] = t_id
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
						newtopic['read_c']=read_c
						print("read_c="+read_c)
					elif(i==1):
						dic_c = np
						newtopic['dis_c']=dic_c
						print("dic_c="+dic_c)
					elif(i==2):
						fans_c = np
						newtopic['fans_c']=fans_c
						print("fans_c="+fans_c)
					else:
						print("不知道的属性")
				host = response.xpath("//div[@class='title W_fb W_autocut ']/a")
				print(len(host))
				if(len(host)==0):
					newtopic['host_n']="没有主持人"
					newtopic['host_id']="没有主持人"
					print("没有主持人")
				else:	
					host_n = host[0].xpath("./@title").extract()[0]
					newtopic['host_n'] = host_n
					print("host_name="+host_n)
					host_id = host[0].xpath("./@usercard").extract()[0]
					host_id = host_id[host_id.find("id=")+3:host_id.find("&type")]
					newtopic['host_id'] = host_id
					print("host_id="+host_id)
				con = response.xpath("//div[@id='Pl_Third_Inline__3']/div/div/div")
				#print(con)
				content = ""
				if(len(con)==0):
					print("没有话题导语")
					content = "没有话题导语"
				else:
					print("有导语：",end="")
					content = con.xpath("string(.)").extract()[0]
					content = content.replace("\t","")
					content = content.replace("\n","")
					print(content)
				newtopic['content']=content
				yield newtopic
				fans_url = response.xpath("//a[@class='t_link S_txt1']/@href").extract()[0]
				#print("fans_url="+fans_url)
				freq = scrapy.Request(url="https:"+fans_url,callback=self.parse4,errback=self.errback)
				freq.meta['useragent']=random.choice(self.agent)
				freq.meta['cookie']=self.cookie
				freq.meta['name']=response.meta['name']
				freq.meta['time']='5'
				freq.meta['page']=1
				freq.meta['count']=0
				freq.meta['t_id']=t_id
				yield freq

			tps = response.xpath("//div[@class='WB_cardwrap WB_feed_type S_bg2 WB_feed_like']")
			tps2 = response.xpath("//div[@class='WB_cardwrap WB_feed_type S_bg2 WB_feed_vipcover WB_feed_like']")
			print("tps=",len(tps))
			print("tps2=",len(tps2))
			tps = tps+tps2
			print("tps=",len(tps))
			counter=0
			for i,tp in enumerate(tps):
				u_id = tp.xpath("./@tbinfo").extract()[0]
				u_id = u_id.replace("\n","")
				u_id = u_id[u_id.find("id=")+3:len(u_id)]
				print(response.meta['name'],response.meta['count']+counter+1,":",end=" ")
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
				print("fr="+fr,end="\t")
				de = tp.xpath(".//a[@action-type='fl_forward']//em")
				if(len(de)==0):
					z_c = "0"
					c_c = "0"
					lk_c = "0"
				else:
					z_c = de[1].xpath("string(.)").extract()[0]
					z_c = z_c.replace(" ","")
					z_c = z_c.replace("\n","")
					if(z_c.find("转发")!=-1):
						z_c = "0"
					de = tp.xpath(".//a[@action-type='fl_comment']//em")
					c_c = de[1].xpath("string(.)").extract()[0]
					c_c = c_c.replace(" ","")
					c_c = c_c.replace("\n","")
					if(c_c.find("评论")!=-1):
						c_c = "0"
					de = tp.xpath(".//a[@action-type='fl_like']")
					if(len(de)>1):
						de = de[1].xpath(".//em")
					else:
						de = de.xpath(".//em")
					lk_c = de[1].xpath("string(.)").extract()[0]
					lk_c = lk_c.replace(" ","")
					lk_c = lk_c.replace("\n","")
					if(lk_c.find("赞")!=-1):
						lk_c = "0"
				print("lk_c="+lk_c,end="\t")
				print("c_c="+c_c,end="\t")
				print("z_c="+z_c,end="\t")
				#获取评论
				curl = "https://m.weibo.cn/api/comments/show?id="+tp_id+"&page=1"
				req = scrapy.Request(url=curl,callback=self.parse5,errback=self.errback)
				req.meta['useragent']=random.choice(self.agent)
				req.meta['cookie']=self.cookie
				req.meta['name']=response.meta['name']
				req.meta['time']='6'
				req.meta['page']=1
				req.meta['count']=0
				req.meta['t_id']=t_id
				req.meta['tp_id']=tp_id
				yield req
				#判断是否是转发
				mark = tp.xpath(".//div[@class='WB_feed_expand']")
				if(len(mark)==0):
					print("不是转发")
				else:
					print("是转发")
					newypost = Topic_postItem()
					y_id = mark.xpath(".//div[@class='WB_info']//a[@node-type='feed_list_originNick']/@suda-uatrack").extract()[0]
					y_id = y_id[y_id.find("nick:")+5:len(y_id)]
					newypost['tp_id'] = y_id
					print("y_id = "+y_id,end="\t")
					yu_id = mark.xpath(".//div[@class='WB_info']//a[@node-type='feed_list_originNick']/@usercard").extract()[0]
					yu_id =yu_id[yu_id.find("id=")+3:yu_id.find("&refer")]
					newypost['u_id'] = yu_id
					print("yu_id = "+yu_id,end="\t")
					yu_name = mark.xpath(".//div[@class='WB_info']//a[@node-type='feed_list_originNick']/@title").extract()[0]
					yu_name = yu_name.replace(" ","")
					yu_name = yu_name.replace("\n","")
					newypost['u_name'] = yu_name
					print("yu_name = "+yu_name,end="\t")
					y_time = mark.xpath(".//a[@node-type='feed_list_item_date']/@title").extract()[0]
					y_time = y_time.replace(" ","")
					y_time = y_time.replace("\n","")
					newypost['time'] = y_time
					print("y_time ="+y_time,end="\t")
					y_fr = mark.xpath(".//a[@action-type='app_source']/text()").extract()[0]
					y_fr = y_fr.replace(" ","")
					y_fr = y_fr.replace("\n","")
					newypost['fr'] = y_fr
					print("y_fr ="+y_fr,end="\t")
					y_de = mark.xpath(".//a[@bpfilter='page_frame']")
					y_z_c = y_de[0].xpath("string(.)").extract()[0]
					y_z_c = y_z_c.replace("转发","")
					y_z_c = y_z_c.replace(" ","")
					y_z_c = y_z_c.replace("\n","")
					y_c_c = y_de[1].xpath("string(.)").extract()[0]
					y_c_c = y_c_c.replace("评论","")
					y_c_c = y_c_c.replace(" ","")
					y_c_c = y_c_c.replace("\n","")
					y_lk_cs = mark.xpath(".//span[@node-type='like_status']")
					y_lk_c = y_lk_cs.xpath("string(.)").extract()[0]
					if(y_lk_c.find("赞")!=0):
						y_lk_c.replace("赞","")
					y_lk_c = y_lk_c.replace(" ","")
					y_lk_c = y_lk_c.replace("\n","")
					newypost['comment_c'] = y_c_c
					newypost['trans_c'] = y_z_c
					newypost['zan_c'] = y_lk_c
					print("y_z_c="+y_z_c+"\ty_c_c="+y_c_c+"\ty_lk_c="+y_lk_c)
					newypost['zhuan_id'] = "No"
					newcontent = mark.xpath(".//div[@class='WB_text']")
					if(len(newcontent)==0):
						newypost['content']="没有内容"
					else:
						newypost['content']=newcontent.xpath("string(.)").extract()[0]
					newypost['t_id']="原"
					if(y_id not in self.tplist):
						self.tplist.append(y_id)
						yield newypost

				if(tp_id not in self.tplist):
					self.tplist.append(tp_id)
					counter=counter+1
					newpost = Topic_postItem()
					newpost['t_id'] = t_id
					newpost['tp_id'] = tp_id
					newpost['u_id'] = u_id
					newpost['u_name'] = u_name
					newpost['time'] = time
					newpost['fr'] = fr
					newpost['comment_c'] = c_c
					newpost['trans_c'] = z_c
					newpost['zan_c'] = lk_c
					if(len(mark)==0):
						newpost['zhuan_id'] = "No"
					else:
						newpost['zhuan_id'] = y_id
					content=tp.xpath(".//div[@class='WB_text W_f14']")
					if(len(content)==0):
						newpost['content']="没有内容"
					else:
						newpost['content']="内容为"+content.xpath("string(.)").extract()[0]
					yield newpost
			#判断有无下一页或者是否达到五百条
			nextpages = response.xpath("//a[@class='page next S_txt1 S_line1']")
			if(len(nextpages)==0):
				print("没有下一页了")
			else:
				response.meta['count']=response.meta['count']+counter
				if(response.meta['count']>=500):
					print(response.meta['name']+"已经",response.meta['count'],"条了")
				else:
					print("现有条数=",response.meta['count'])
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

	def parse4(self, response):
		#先判断是否读取成功
		lis = response.xpath("//ul[@class='follow_list']/li")
		count = len(lis)
		if(count==0):
			print(response.meta['name']+"粉丝列表读取失败，重新读取")
			req2 = scrapy.Request(url=response.url,callback=self.parse4,errback=self.errback,dont_filter = True)
			req2.meta['useragent']=random.choice(self.agent)
			req2.meta['cookie']=self.cookie
			req2.meta['name']=response.meta['name']
			req2.meta['time']='5'
			req2.meta['page']=response.meta['page']
			req2.meta['count']=response.meta['count']
			req2.meta['t_id']=response.meta['t_id']
			yield req2
		else:
			i=1
			for li in lis:
				newfans = Fans_listItem()
				u_name = li.xpath(".//a[@class='S_txt1']/@title").extract()[0]
				newfans['u_name'] = u_name
				print(response.meta['name'],response.meta['count']+i,"fans:",end=" ")
				print("u_name="+u_name,end="\t")
				u_id = li.xpath(".//a[@class='S_txt1']/@usercard").extract()[0]
				u_id = u_id[u_id.find("id=")+3:u_id.find("&refer")]
				newfans['u_id'] = u_id
				print("u_id="+u_id,end="\t")
				rank_n = i+response.meta['count']
				i=i+1
				newfans['rank_n'] = rank_n
				print("rank_n=",rank_n)
				newfans['t_id'] = response.meta['t_id']
				if(u_id not in self.userlist):
					self.userlist.append(u_id)
					yield newfans
			print("判断下一页")
			nextpages = response.xpath("//a[@class='page next S_txt1 S_line1']")
			print(len(nextpages))
			if(len(nextpages)==0):
				print(response.meta['name']+"粉丝列表最后一页了")
			else:
				response.meta['count']=response.meta['count']+count
				if(response.meta['count']>=100):
					print(response.meta['name']+"粉丝已经",response.meta['count'],"人了")
				else:
					nextpage = response.xpath("//a[@class='page next S_txt1 S_line1']/@href").extract()[0]
					print(nextpage)
					url = "https://weibo.com"+nextpage
					req = scrapy.Request(url=url,callback=self.parse4,errback=self.errback)
					req.meta['useragent']=random.choice(self.agent)
					req.meta['cookie']=self.cookie
					req.meta['name']=response.meta['name']
					req.meta['time']='5'
					req.meta['page']=response.meta['page']+1
					req.meta['count']=response.meta['count']
					req.meta['t_id']=response.meta['t_id']
					yield req

	def parse5(self, response):
		print("评论获取")
		x = response
		b = x.xpath("//pre/text()")
		if(len(b)==0):
			print("评论获取失败，重新读取")
			req2 = scrapy.Request(url=response.url,callback=self.parse5,errback=self.errback,dont_filter = True)
			req2.meta['useragent']=random.choice(self.agent)
			req2.meta['cookie']=self.cookie
			req2.meta['name']=response.meta['name']
			req2.meta['time']='6'
			req2.meta['page']=response.meta['page']
			req2.meta['count']=response.meta['count']
			req2.meta['t_id']=response.meta['t_id']
			req2.meta['tp_id']=response.meta['tp_id']
			yield req2
		else:
			a = x.xpath("//pre/text()").extract()[0]
			a = a.encode("utf-8")
			file = open("new2.txt","wb")
			file.write(a)
			file.close()
			file = open("new2.txt","r")
			a = file.read()
			file.close()
			kill = a.find("\\ud")
			while kill!=-1:
				print("kill!")
				a = a[0:kill]+a[kill+6:len(a)]
				kill = a.find("\\ud")
			a = a.encode("utf-8").decode("unicode-escape")
			i = 0
			counter=0
			while 1:
				#print(i)
				i = a.find("\"id\"",i)
				if(i==-1):
					break
				idd = a[a.find("\"id\"",i)+5:a.find(",\"created_at",i)]
				print("id="+idd,end="\t\t")
				counter=counter+1
				creat = a[a.find("\"created_at\"",i)+14:a.find("\",\"source",i)]
				print("created_at="+creat,end="\t\t")
				source = a[a.find("\"source\"",i)+10:a.find("\",\"user",i)]
				print("source="+source,end="\t\t")
				i = a.find("\"user\"",i)
				if(i==-1):
					break
				u_id = a[a.find("\"id\"",i)+5:a.find(",\"screen_name",i)]
				print("u_id="+u_id,end="\t\t")
				u_name = a[a.find("\"screen_name\"",i)+15:a.find("\",\"profile_image_url",i)]
				print("u_name="+u_name,end="\t\t")
				text = a[a.find("\"text\"",i)+8:a.find("\",\"like_counts",i)]
				#print("text="+text)
				print("")
				i=a.find("\"text\"",i)
				if(i==-1):
					break
				if(idd not in self.clist):
					self.clist.append(idd)
					newcom = Comment_listItem()
					newcom['tp_id'] = response.meta['tp_id']
					newcom['comment_id'] = idd
					newcom['u_id'] = u_id
					newcom['u_name'] = u_name
					newcom['content'] = text
					yield newcom
			response.meta['count']=response.meta['count']+counter
			if(response.meta['count']>50):
				print("评论已达到",response.meta['count'],"条")
			else:
				if(counter==0):
					print("已到达尾页")
				else:
					print("查看下一页评论")
					url = "https://m.weibo.cn/api/comments/show?id="+response.meta['tp_id']+"&page="+str(response.meta['page']+1)
					req = scrapy.Request(url=url,callback=self.parse5,errback=self.errback)
					req.meta['useragent']=random.choice(self.agent)
					req.meta['cookie']=self.cookie
					req.meta['name']=response.meta['name']
					req.meta['time']='6'
					req.meta['page']=response.meta['page']+1
					req.meta['count']=response.meta['count']
					req.meta['t_id']=response.meta['t_id']
					req.meta['tp_id']=response.meta['tp_id']
					yield req


	def errback(self, failure):
		print(failure)