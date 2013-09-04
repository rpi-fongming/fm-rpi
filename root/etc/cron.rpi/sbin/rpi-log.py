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
	shell_cmd ("sqlite3 " + file_db + " < " + file_script)
	sql = "select * from tb_rpiEvent"
	result = sql_cmd(con,sql)
	for row in result:
		print row

######################################################################################
## Main function start here

file_path = os.path.dirname(sys.argv[0])
file_db=file_path+"/rpi-event.db"
file_script=file_path+"/rpi-eventScript"
#print (file_path, file_db,file_script,sys.argv[0])
con = sqlite.connect(file_db)

if (len(sys.argv) == 1):
	print (sys.argv[0]+ " eMsg eType")
	sys.exit(0)

if (len(sys.argv) == 2):
	eMsg = sys.argv[1]
	if (eMsg=="init_db"):
		sql_init(con);
	if (eMsg=="test") or (eMsg=="show"):
		sql = "select * from tb_rpiEvent"
		result = sql_cmd(con,sql)
		for row in result:
			print row
	sys.exit(0)


eMsg = sys.argv[1]
eType = sys.argv[2]

#print ("-----------------------")
#print (file_db, eMsg, eType)

if (not os.path.exists(file_db)):
	print ("file does not exist")
	sql_init(con);

sql = "insert into tb_rpiEvent(eMsg,eType) values(\"" + eMsg + "\",\"" + eType + "\");"
result= sql_cmd(con, sql)
sql = "select * from tb_rpiEvent ORDER BY eID DESC limit 1;"
result= sql_cmd(con, sql)
for row in result:
	print row
