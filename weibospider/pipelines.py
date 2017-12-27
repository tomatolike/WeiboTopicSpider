# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as MySQLdb
from weibospider.items import BaseinfoItem,Fans_listItem,Topic_postItem,Comment_listItem

class WeibospiderPipeline(object):
    def process_item(self, item, spider):
    	db = MySQLdb.connect(host="localhost",user="root",passwd="1997lk421",db="weibo",charset="utf8")
    	cursor=db.cursor()
    	#If it is baseinfo
    	if isinstance(item,BaseinfoItem):
    		sql = "insert into Baseinfo(id,name,read_c,dis_c,fans_c,host_n,host_id,content) values(\"%s\",\"%s\",%d,%d,%d,%d,\"%s\",\"%s\");"
    		cursor.execute(sql,item['t_id'],item['name'],item['read_c'],item['dis_c'],item['fans_c'],item['host_n'],item['host_id'],item['content'])
    		db.commit()
    	#If it is fans_list
    	elif isinstance(item,Fans_listItem):
    		sql = "insert into Fnas_list(t_id,u_name,u_id,rank_n) values(\"%s\",\"%s\",\"%s\",%d);"
    		cursor.execute(sql,item['t_id'],item['u_name'],item['u_id'],item['rank_n'])
    		db.commit()
    	#If it is topic_post
    	elif isinstance(item,Topic_postItem):
    		sql = "insert into Baseinfo(t_id,tp_id,u_name,u_id,time,fr,comment_c,trans_c,zan_c,zhuan_id,content) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",%d,%d,%d,\"%s\",\"%s\");"
    		cursor.execute(sql,item['t_id'],item['tp_id'],item['u_name'],item['u_id'],item['time'],item['fr'],item['comment_c'],item['trans_c'],item['zan_c'],item['zhuan_id'],item['content'])
    		db.commit()
    	elif isinstance(item,Comment_listItem):
    		sql = "insert into Baseinfo(tp_id,comment_id,u_id,u_name,content) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");"
    		cursor.execute(sql,item['tp_id'],item['comment_id'],item['u_id'],item['u_name'],item['content'])
    		db.commit()
    	else:
    		print("Wrong Item Type!")
    	return item
        
