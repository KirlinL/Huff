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

Cstation=['中山公园','南京东路','五角场','延长路',
         '南京西路','徐家汇','金沙江路','陆家嘴',
         '虹口足球场','七宝','打浦桥','四川北路',
         '豫园','莘庄','娄山关路','长寿路',
         '真北路','龙阳路','莲花路']

Estation=['ZhongshanPark','EastNanjingRoad','Wujiaochang','YanchangRoad',
          'WestNanjingRoad','Xujiahui','JinshajiangRoad','Lujiazui',
          'HongkouFootballStadium','Qibao','Dapuqiao','NorthSichuanRoad',
          'Yuyuan','Xinzhuang','LoushanguanRoad','ChangshouRoad',
          'ZhenbeiRoad','LongyangRoad','LianhuaRoad']


con = MySQLdb.connect("localhost","root","likelin0610","zc",charset="utf8" )

cur = con.cursor()

for i in range(len(table)):
    sql='create table count_'+table[i]+' select `zhongshanpark_'+table[i]+'`.`address_in`,\
                `zhongshanpark_'+table[i]+'`.`address_out` as a1,`zhongshanpark_'+table[i]+'`.`count(*)`as c1,\
                `eastnanjingroad_'+table[i]+'`.`address_out` as a2,`eastnanjingroad_'+table[i]+'`.`count(*)` as c2,\
                `wujiaochang_'+table[i]+'`.`address_out` as a3,`wujiaochang_'+table[i]+'`.`count(*)` as c3,\
                `yanchangroad_'+table[i]+'`.`address_out` as a4,`yanchangroad_'+table[i]+'`.`count(*)` as c4,\
                `westnanjingroad_'+table[i]+'`.`address_out` as a5,`westnanjingroad_'+table[i]+'`.`count(*)` as c5,\
                `xujiahui_'+table[i]+'`.`address_out` as a6,`xujiahui_'+table[i]+'`.`count(*)` as c6,\
                `jinshajiangroad_'+table[i]+'`.`address_out` as a7,`jinshajiangroad_'+table[i]+'`.`count(*)` as c7,\
                `lujiazui_'+table[i]+'`.`address_out` as a8,`lujiazui_'+table[i]+'`.`count(*)` as c8,\
                `hongkoufootballstadium_'+table[i]+'`.`address_out` as a9,`hongkoufootballstadium_'+table[i]+'`.`count(*)` as c9,\
                `qibao_'+table[i]+'`.`address_out` as a10,`qibao_'+table[i]+'`.`count(*)` as c10,\
                `dapuqiao_'+table[i]+'`.`address_out` as a11,`dapuqiao_'+table[i]+'`.`count(*)` as c11,\
                `northsichuanroad_'+table[i]+'`.`address_out` as a12,`northsichuanroad_'+table[i]+'`.`count(*)` as c12,\
                `yuyuan_'+table[i]+'`.`address_out` as a13,`yuyuan_'+table[i]+'`.`count(*)` as c13,\
                `xinzhuang_'+table[i]+'`.`address_out` as a14,`xinzhuang_'+table[i]+'`.`count(*)` as c14,\
                `loushanguanroad_'+table[i]+'`.`address_out` as a15,`loushanguanroad_'+table[i]+'`.`count(*)` as c15,\
                `changshouroad_'+table[i]+'`.`address_out` as a16,`changshouroad_'+table[i]+'`.`count(*)` as c16,\
                `zhenbeiroad_'+table[i]+'`.`address_out` as a17,`zhenbeiroad_'+table[i]+'`.`count(*)` as c17,\
                `longyangroad_'+table[i]+'`.`address_out` as a18,`longyangroad_'+table[i]+'`.`count(*)` as c18,\
                `lianhuaroad_'+table[i]+'`.`address_out` as a19,`lianhuaroad_'+table[i]+'`.`count(*)` as c19\
            from `zhongshanpark_'+table[i]+'`\
            left join `eastnanjingroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`eastnanjingroad_'+table[i]+'`.`address_in`\
            left join `wujiaochang_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`= `wujiaochang_'+table[i]+'`.`address_in`\
            left join `yanchangroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`yanchangroad_'+table[i]+'`.`address_in`\
            left join `westnanjingroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`= `westnanjingroad_'+table[i]+'`.`address_in`\
            left join `xujiahui_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`xujiahui_'+table[i]+'`.`address_in`\
            left join `jinshajiangroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`jinshajiangroad_'+table[i]+'`.`address_in`\
            left join `lujiazui_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`lujiazui_'+table[i]+'`.`address_in`\
            left join `hongkoufootballstadium_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`hongkoufootballstadium_'+table[i]+'`.`address_in`\
            left join `qibao_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`qibao_'+table[i]+'`.`address_in`\
            left join `dapuqiao_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`dapuqiao_'+table[i]+'`.`address_in`\
            left join `northsichuanroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`northsichuanroad_'+table[i]+'`.`address_in`\
            left join `yuyuan_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`yuyuan_'+table[i]+'`.`address_in`\
            left join `xinzhuang_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`xinzhuang_'+table[i]+'`.`address_in`\
            left join `loushanguanroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`loushanguanroad_'+table[i]+'`.`address_in`\
            left join `changshouroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`changshouroad_'+table[i]+'`.`address_in`\
            left join `zhenbeiroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`zhenbeiroad_'+table[i]+'`.`address_in`\
            left join `longyangroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`longyangroad_'+table[i]+'`.`address_in`\
            left join `lianhuaroad_'+table[i]+'` on `zhongshanpark_'+table[i]+'`.`address_in`=`lianhuaroad_'+table[i]+'`.`address_in`\
            '
    cur.execute(sql)

    

cur.close()
con.close()
