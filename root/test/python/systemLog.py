#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import sys

con = sqlite.connect('sysEvent.db')

with con:
    
	cur = con.cursor()    
	cur.execute('SELECT SQLITE_VERSION()')		
	data = cur.fetchone()
	print "SQLite version: %s" % data
#	cur.execute("INSERT INTO tb_sysEvent(msg,type) VALUES('hello','twitter')")
	cur.execute("select * from tb_sysEvent")
	rows = cur.fetchall()
	for row in rows:
		print row
