drop database weibo;

create database weibo;
use weibo;

create table BaseinfoItem(
	t_id varchar(50),
	name varchar(50),
	read_c varchar(20),
	dis_c varchar(20),
	fans_c varchar(20),
	host_n varchar(30),
	host_id varchar(50),
	content varchar(500),
	primary key(t_id)
);

create table Comment_listItem(
	t_id varchar(50),
	comment_id varchar(50),
	u_id varchar(50),
	u_name varchar(30),
	content varchar(500),
	primary key(comment_id)
);

create table Fans_listItem(
	t_id varchar(50),
	u_name varchar(30),
	u_id varchar(50),
	rank_n int,
	primary key(t_id,u_id)
);

create table Topic_postItem(
	t_id varchar(50),
	tp_id varchar(50),
	u_name varchar(30),
	u_id varchar(50),
	t_me varchar(30),
	fr varchar(50),
	comment_c varchar(20),
	trans_c varchar(20),
	zan_c varchar(20),
	zhuan_id varchar(50),
	content varchar(500),
	primary key(tp_id)
);

alter table BaseinfoItem convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table Comment_listItem convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table Fans_listItem convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table Topic_postItem convert to character set utf8mb4 collate utf8mb4_unicode_ci;

