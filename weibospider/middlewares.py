# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http import HtmlResponse
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import requests



class WeibospiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class PhantomJSMiddleware(object):
    @classmethod
    def process_request(cls, request, spider):
        print("start"+request.meta['name']+" time:"+request.meta['time']+" page:",request.meta['page'])
        cc=request.meta['cookie']
        #获取第一部分的内容
        cap = dict(DesiredCapabilities.PHANTOMJS)
        cap["phantomjs.page.settings.loadImages"]=False
        cap["phantomjs.page.settings.disk-cache"]=True
        cap["phantomjs.page.customHeaders.Cookie"]=cc
        cap["phantomjs.page.settings.userAgent"]= request.meta['useragent']
        print("ok!")
        driver = webdriver.PhantomJS(desired_capabilities=cap)
        print("ok!!") 
        driver.get(request.url)
        print("等待五秒")
        time.sleep(5)
        content = driver.page_source.encode('utf-8')
        part2 = driver.find_elements_by_xpath("//div[@node-type='lazyload']")
        driver.quit()
        
        if(request.meta['time']=='3' or request.meta['time']=='4'):
            if(request.meta['page']==1):
                #判断是否有第二部分的内容
                if(len(part2)!=0):
                    #获取第二部分的内容
                    cap = dict(DesiredCapabilities.PHANTOMJS)
                    cap["phantomjs.page.settings.loadImages"]=False
                    cap["phantomjs.page.settings.disk-cache"]=True
                    cap["phantomjs.page.customHeaders.Cookie"]=cc
                    cap["phantomjs.page.settings.userAgent"]= request.meta['useragent']
                    driver = webdriver.PhantomJS(desired_capabilities=cap)
                    driver.get("https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain="+request.meta['t_id'][0:6]+"&from=page_huati_rcd_more&pagebar=0&tab=emceercd&current_page=1&since_id=14&pl_name=Pl_Third_App__46&id="+request.meta['t_id']+"&script_uri=/p/"+request.meta['t_id']+"/emceercd&feed_type=1&page=1&pre_page=1&domain_op="+request.meta['t_id'][0:6])
                    print("等待两秒"+"https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain="+request.meta['t_id'][0:6]+"&from=page_huati_rcd_more&pagebar=0&tab=emceercd&current_page=1&since_id=14&pl_name=Pl_Third_App__46&id="+request.meta['t_id']+"&script_uri=/p/"+request.meta['t_id']+"/emceercd&feed_type=1&page=1&pre_page=1&domain_op="+request.meta['t_id'][0:6])
                    time.sleep(2)
                    content2 = driver.page_source.encode('utf-8')
                    driver.quit()
                    file = open("new.txt","wb")
                    file.write(content2)
                    file.close()
                    file = open("new.txt","r")
                    test = file.read()
                    file.close()
                    kill = test.find("\\ud")
                    while kill!=-1:
                        print("kill!")
                        test = test[0:kill]+test[kill+6:len(test)]
                        kill = test.find("\\ud")
                    test = test.encode("utf-8").decode("unicode-escape")
                    content2 = test
                    a = content2.find('{"code":"100000","msg":"","data":"')
                    b = content2.find('\"}<')
                    print(b)
                    content2 = content2[a+34:b]
                    content2 = content2.replace("&lt;","<")
                    content2 = content2.replace("&gt;",">")
                    content2 = content2.replace('"}',"")
                    like = content2.replace('\\/',"/")
                    content2 = like.encode('utf-8')
                    #print("like="+like+"=likeend")
                    part3 = like.find("node-type=\"lazyload\"")
                    
                    #判断是否有第三部分的内容
                    if(part3!=-1):
                        #获取第三部分的内容
                        cap = dict(DesiredCapabilities.PHANTOMJS)
                        cap["phantomjs.page.settings.loadImages"]=False
                        cap["phantomjs.page.settings.disk-cache"]=True
                        cap["phantomjs.page.customHeaders.Cookie"]=cc
                        cap["phantomjs.page.settings.userAgent"]= request.meta['useragent']
                        driver = webdriver.PhantomJS(desired_capabilities=cap)
                        driver.get("https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain="+request.meta['t_id'][0:6]+"&from=page_huati_rcd_more&pagebar=1&tab=emceercd&current_page=2&since_id=29&pl_name=Pl_Third_App__46&id="+request.meta['t_id']+"&script_uri=/p/"+request.meta['t_id']+"/emceercd&feed_type=1&page=1&pre_page=1&domain_op="+request.meta['t_id'][0:6])
                        print("等待两秒")
                        time.sleep(2)
                        content3 = driver.page_source.encode('utf-8')
                        driver.quit()
                        file = open("new.txt","wb")
                        file.write(content3)
                        file.close()
                        file = open("new.txt","r")
                        test = file.read()
                        file.close()
                        kill = test.find("\\ud")
                        while kill!=-1:
                            print("kill!")
                            test = test[0:kill]+test[kill+6:len(test)]
                            kill = test.find("\\ud")
                        test = test.encode("utf-8").decode("unicode-escape")
                        content3 = test
                        a = content3.find('{"code":"100000","msg":"","data":"')
                        b = content3.find('\"}<')
                        content3 = content3[a+34:b]
                        content3 = content3.replace("&lt;","<")
                        content3 = content3.replace("&gt;",">")
                        content3 = content3.replace('"}',"")
                        like = content3.replace('\\/',"/")
                        content3 = like.encode('utf-8')
                        nextpage = like.find("page next S_txt1 S_line1")
                        content = content+content2+content3
                    else:
                        content = content+content2
            else:
                #判断是否有第二部分的内容
                if(len(part2)!=0):
                    #获取第二部分的内容
                    cap = dict(DesiredCapabilities.PHANTOMJS)
                    cap["phantomjs.page.settings.loadImages"]=False
                    cap["phantomjs.page.settings.disk-cache"]=True
                    cap["phantomjs.page.customHeaders.Cookie"]=cc
                    cap["phantomjs.page.settings.userAgent"]= request.meta['useragent']
                    driver = webdriver.PhantomJS(desired_capabilities=cap)
                    driver.get("https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain="+request.meta['t_id'][0:6]+"&current_page="+str((request.meta['page']-1)*2+request.meta['page'])+"&since_id="+str(14+request.meta['page']*45-45)+"&page="+str(request.meta['page'])+"&pagebar=0&tab=emceercd&pl_name=Pl_Third_App__46&id="+request.meta['t_id']+"&script_uri=/p/"+request.meta['t_id']+"/emceercd&feed_type=1&pre_page="+str(request.meta['page'])+"&domain_op="+request.meta['t_id'][0:6])
                    print("等待两秒")
                    time.sleep(2)
                    content2 = driver.page_source.encode('utf-8')
                    driver.quit()
                    file = open("new.txt","wb")
                    file.write(content2)
                    file.close()
                    file = open("new.txt","r")
                    test = file.read()
                    file.close()
                    kill = test.find("\\ud")
                    while kill!=-1:
                        print("kill!")
                        test = test[0:kill]+test[kill+6:len(test)]
                        kill = test.find("\\ud")
                    test = test.encode("utf-8").decode("unicode-escape")
                    content2 = test
                    a = content2.find('{"code":"100000","msg":"","data":"')
                    b = content2.find('\"}<')
                    content2 = content2[a+34:b]
                    content2 = content2.replace("&lt;","<")
                    content2 = content2.replace("&gt;",">")
                    content2 = content2.replace('"}',"")
                    like = content2.replace('\\/',"/")
                    content2=like.encode('utf-8')
                    part3 = like.find("node-type=\"lazyload\"")

                    #判断是否有第三部分的内容
                    if(part3!=-1):
                        #获取第三部分的内容
                        cap = dict(DesiredCapabilities.PHANTOMJS)
                        cap["phantomjs.page.settings.loadImages"]=False
                        cap["phantomjs.page.settings.disk-cache"]=True
                        cap["phantomjs.page.customHeaders.Cookie"]=cc
                        cap["phantomjs.page.settings.userAgent"]= request.meta['useragent']
                        driver = webdriver.PhantomJS(desired_capabilities=cap)
                        driver.get("https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain="+request.meta['t_id'][0:6]+"&current_page="+str((request.meta['page']-1)*2+request.meta['page']+1)+"&since_id="+str(14+request.meta['page']*45-45+15)+"&page="+str(request.meta['page'])+"&pagebar=1&tab=emceercd&pl_name=Pl_Third_App__46&id="+request.meta['t_id']+"&script_uri=/p/"+request.meta['t_id']+"/emceercd&feed_type=1&pre_page="+str(request.meta['page'])+"&domain_op="+request.meta['t_id'][0:6])
                        print("https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain="+request.meta['t_id'][0:6]+"&current_page="+str((request.meta['page']-1)*2+request.meta['page']+1)+"&since_id="+str(14+request.meta['page']*45-45+15)+"&page="+str(request.meta['page'])+"&pagebar=1&tab=emceercd&pl_name=Pl_Third_App__46&id="+request.meta['t_id']+"&script_uri=/p/"+request.meta['t_id']+"/emceercd&feed_type=1&pre_page="+str(request.meta['page'])+"&domain_op="+request.meta['t_id'][0:6])
                        print("等待两秒")
                        time.sleep(2)
                        content3 = driver.page_source.encode('utf-8')
                        driver.quit()
                        file = open("new.txt","wb")
                        file.write(content3)
                        file.close()
                        file = open("new.txt","r")
                        test = file.read()
                        file.close()
                        kill = test.find("\\ud")
                        while kill!=-1:
                            print("kill!")
                            test = test[0:kill]+test[kill+6:len(test)]
                            kill = test.find("\\ud")
                        test = test.encode("utf-8").decode("unicode-escape")
                        content3 = test
                        a = content3.find('{"code":"100000","msg":"","data":"')
                        b = content3.find('\"}<')
                        content3 = content3[a+34:b]
                        content3 = content3.replace("&lt;","<")
                        content3 = content3.replace("&gt;",">")
                        content3 = content3.replace('"}',"")
                        like = content3.replace('\\/',"/")                        
                        content3 = like.encode('utf-8')
                        nextpage = like.find("page next S_txt1 S_line1")
                        #print(like)
                        content = content+content2+content3
                        #file = open("new.txt","w")
                        #file.write(like)
                        #file.close()
                    else:
                        content = content+content2
        
        #print(content)
        
        print("end!")
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
