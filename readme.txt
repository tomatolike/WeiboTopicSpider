微博Topic爬虫 from 李珂 3150103729 G12

爬取内容：
1、微博话题榜前十个话题，包括 话题ID，话题名称，阅读量，讨论量，粉丝量，主持人名称，主持人ID，话题导语。
2、这十个微博话题榜各自的粉丝列表，前100人，包括 粉丝ID，粉丝名称
3、这十个微博话题榜各自的微博条目，前500个，包括 微博条目ID，博主名称，博主ID，发微博时间，微博来源，评论条数，转发数目，赞数，原poID，微博内容
4、每条微博下面的评论，前50个，包括 评论ID，评论的用户ID，评论的用户名，评论内容

部署环境：
Language: Python 3.6.3
Tools:	Scrapy 1.4.0
		Selenium 2.28.0
		Phantomjs 2.1.1
OS: macOS High Sierra 10.13

部署步骤：
1、配置好部署环境
2、根据统计目录下的database.sql文件建立好数据库
3、修改pipelines.py里面的数据库连接参数
4、手动登录一次微博，抓包并复制自己的cookie，复制粘贴到weibo.py的self.cookie位置

运行：
scrapy crawl weibo