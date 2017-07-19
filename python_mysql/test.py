#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import sys

con = MySQLdb.connect("localhost","root","likelin0610","zc",charset="utf8" )

cur = con.cursor()




sql_i="INSERT INTO `time_cost` \
      VALUES('112','asda','agsasd')\
      "
cur.execute(sql_i)

con.commit()

cur.close()
con.close()
