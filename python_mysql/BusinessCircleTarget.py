#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import sys

table=['20','21','22','23','24','25','26']

station=['2号线中山公园','2号线南京东路','10号线五角场','1号线延长路',
         '2号线南京西路','1号线徐家汇','3号线金沙江路','2号线陆家嘴',
         '3号线虹口足球场','9号线七宝','9号线打浦桥','10号线四川北路',
         '10号线豫园','1号线莘庄','2号线娄山关路','7号线长寿路',
         '13号线真北路','2号线龙阳路','1号线莲花路']

Estation=['ZhongshanPark','EastNanjingRoad','Wujiaochang','YanchangRoad',
          'WestNanjingRoad','Xujiahui','JinshajiangRoad','Lujiazui',
          'HongkouFootballStadium','Qibao','Dapuqiao','NorthSichuanRoad',
          'Yuyuan','Xinzhuang','LoushanguanRoad','ChangshouRoad',
          'ZhenbeiRoad','LongyangRoad','LianhuaRoad']


con = MySQLdb.connect("localhost","root","likelin0610","zc",charset="utf8" )

cur = con.cursor()


for i in range(len(table)):
    for j in range(len(station)):
        
        sql='CREATE TABLE '+Estation[j]+'_'+table[i]+' \
            SELECT address_in,address_out,COUNT(*)\
            FROM `huff_'+table[i]+'` \
            WHERE address_out="'+station[j]+'"\
            GROUP BY address_in\
            '
        cur.execute(sql)

    

cur.close()
con.close()
