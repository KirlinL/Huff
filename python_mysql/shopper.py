#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import sys

table=['20','21','22','23','24','25','26']


for i in range(7):
    con = MySQLdb.connect("localhost","root","likelin0610","result",charset="utf8" )
    cur = con.cursor()
    sql='CREATE TABLE huff_'+table[i]+' \
        SELECT * FROM '+table[i]+'_25\
        WHERE `'+table[i]+'_25`.`cardid`\
        NOT IN (SELECT cardid FROM `work_id_all`)'
    cur.execute(sql)

    

cur.close()
con.close()
