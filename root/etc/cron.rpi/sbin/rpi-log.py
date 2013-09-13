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
	sql = "select * from tb_rpiStatus"
	result = sql_cmd(con,sql)
	for row in result:
		print row


def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])

######################################################################################
## Main function start here
cpu_sn = getSerial()
file_path = os.path.dirname(sys.argv[0])
#file_db=file_path+"/rpi-"+cpu_sn+".log.db"
file_db=file_path + "/rpi-log.db"
file_script=file_path+"/rpi-eventScript"
#print (file_path, file_db,file_script,sys.argv[0],os.path.dirname(sys.argv[0])+"/rpi-log.db")
#print (cpu_sn, file_db)
con = sqlite.connect(file_db)

if (len(sys.argv) == 1):
	print (os.path.basename(sys.argv[0])+ " {eType} {eMsg} ")
	sys.exit(0)

if (len(sys.argv) == 2):
	eType = sys.argv[1]
	if (eType=="rpi-boot"):
		print "booting rpi";
		sql = "update tb_rpiStatus set boot_twitter = '0'"
		sql_cmd(con,sql)
		result = sql_cmd(con,"select boot_twitter from tb_rpiStatus limit 1")
		print result[0][0]
        
        
	if (eType=="show_db"):
		print file_db;
	if (eType=="init_db"):
		sql_init(con);
	if (eType=="test") or (eType=="show"):
		sql = "select * from tb_rpiEvent ORDER BY eID DESC limit 10"
		result = sql_cmd(con,sql)
		for row in reversed(result):
			print row
	sys.exit(0)

eMsg = sys.argv[2]
eType = sys.argv[1]

if (eType=="select"):
	print (eMsg);

if (not os.path.exists(file_db)):
	print ("file does not exist")
	sql_init(con);

sql = "insert into tb_rpiEvent(eMsg,eType) values(\"" + eMsg + "\",\"" + eType + "\");"
result= sql_cmd(con, sql)
sql = "select * from tb_rpiEvent ORDER BY eID DESC limit 1;"
result= sql_cmd(con, sql)
for row in result:
	print row
