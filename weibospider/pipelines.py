# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as MySQLdb
from weibospider.items import BaseinfoItem,Fans_listItem,Topic_postItem,Comment_listItem
import re

class WeibospiderPipeline(object):
    def process_item(self, item, spider):
    	db = MySQLdb.connect(host="localhost",user="root",passwd="1997lk421",db="weibo",charset="utf8mb4")
    	cursor=db.cursor()
    	reChinese = re.compile('[\u4e00-\u9fa5]+')
    	#If it is baseinfo
    	if isinstance(item,BaseinfoItem):
    		sql = "insert into BaseinfoItem(t_id,name,read_c,dis_c,fans_c,host_n,host_id,content) values("
    		sql = sql+"\""+item['t_id'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['name'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['read_c'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['dis_c'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['fans_c'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['host_n'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['host_id'].replace("\"","\\\"")+"\","
    		li=reChinese.findall(item['content'])
    		item['content']="".join(li)
    		if(len(item['content'])>=500):
    			item['content']=item['content'][0:500]
    		sql = sql+"\""+item['content'].replace("\"","\\\"")+"\""
    		sql = sql+");"
    		cursor.execute(sql)
    		db.commit()
    		print("insert topic "+item['name'])
    	#If it is fans_list
    	elif isinstance(item,Fans_listItem):
    		sql = "insert into Fans_listItem(t_id,u_name,u_id,rank_n) values("
    		sql = sql + "\""+item['t_id'].replace("\"","\\\"")+"\","
    		sql = sql + "\""+item['u_name'].replace("\"","\\\"")+"\","
    		sql = sql + "\""+item['u_id'].replace("\"","\\\"")+"\","
    		sql = sql + str(item['rank_n'])
    		sql = sql+");"
    		cursor.execute(sql)
    		db.commit()
    		print("insert fans "+item['u_id'])
    	#If it is topic_post
    	elif isinstance(item,Topic_postItem):
    		sql = "insert into Topic_postItem(t_id,tp_id,u_name,u_id,t_me,fr,comment_c,trans_c,zan_c,zhuan_id,content) values("
    		sql = sql+"\""+item['t_id'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['tp_id'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['u_name'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['u_id'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['time'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['fr'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['comment_c'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['trans_c'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['zan_c'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['zhuan_id'].replace("\"","\\\"")+"\","
    		li=reChinese.findall(item['content'])
    		item['content']="".join(li)
    		if(len(item['content'])>=500):
    			item['content']=item['content'][0:500]
    		sql = sql+"\""+item['content'].replace("\"","\\\"")+"\""
    		sql = sql+");"
    		cursor.execute(sql)
    		db.commit()
    		print("insert post "+item['tp_id'])
    	elif isinstance(item,Comment_listItem):
    		sql = "insert into Comment_listItem(tp_id,comment_id,u_id,u_name,content) values("
    		sql = sql+"\""+item['tp_id'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['comment_id'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['u_id'].replace("\"","\\\"")+"\","
    		sql = sql+"\""+item['u_name'].replace("\"","\\\"")+"\","
    		li=reChinese.findall(item['content'])
    		item['content']="".join(li)
    		if(len(item['content'])>=500):
    			item['content']=item['content'][0:500]
    		sql = sql+"\""+item['content'].replace("\"","\\\"")+"\""
    		sql = sql+");"
    		cursor.execute(sql)
    		db.commit()
    		print("insert comment "+item['comment_id'])
    	else:
    		print("Wrong Item Type!")
    	return item

