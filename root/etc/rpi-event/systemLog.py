#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#python systemLog.py 'eMsg' 'eType'
#

import sqlite3 as sqlite
import sys, os

def shell_cmd(cmd):
	_result = os.popen("su -c \"" + cmd + "\"").read()
	_result = _result.replace("\r","")
	_result = _result.replace("\n","")
	print(_result)
	return(_result)

def sql_cmd(db_con, sql):
	with db_con:
		cur = db_con.cursor()    
		cur.execute(sql)
		rows = cur.fetchall()
	return (rows)	

def sql_init(db_con):
	shell_cmd ("sqlite3 " + file_db + " < " + file_path + "/sysEventScript")
	sql = "select * from tb_sysEvent"
	result = sql_cmd(con,sql)
	for row in result:
		print row

######################################################################################
## Main function start here

if (len(sys.argv) >=3):
	eMsg = sys.argv[1]
	eType = sys.argv[2]
else:
	print ("Not enough arg")
	sys.exit(0)

file_path = os.path.dirname(sys.argv[0])
file_db=file_path+"/sysEvent.db"
#print (file_db, eMsg, eType)
con = sqlite.connect(file_db)

if (eMsg=="init_db"):
	sql_init(con);
	sys.exit(0)

if (eMsg=="test"):
	sql = "select * from tb_sysEvent"
	result = sql_cmd(con,sql)
	for row in result:
		print row
	sys.exit(0)

if (not os.path.exists(file_db)):
	print ("file does not exist")
	sql_init(con);


sql = "insert into tb_sysEvent(eMsg,eType) values(\"" + eMsg + "\",\"" + eType + "\");"
result= sql_cmd(con, sql)
sql = "select * from tb_sysEvent ORDER BY eID DESC limit 1;"
result= sql_cmd(con, sql)
for row in result:
	print row
