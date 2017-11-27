# -*- coding: utf-8 -*-



import pandas as pd
from pymysqlpool import ConnectionPool
config = {
 'pool_name': 'qqMsgDBPool',
 'host': '47.93.240.110',
 'port': 3306,
 'user': 'root',
 'password': 'a1b2c3',
 'database': 'sydb1'
}
def connection_pool():
	# Return a connection pool instance
	pool = ConnectionPool(**config)
	pool.connect()
	return pool
	
try:
	conPool = connection_pool()
except e:
	print("error")
def insertData(contact, member, content):
	con = conPool.connection()
	pd.read_sql('SELECT * FROM user', con)



def onQQMessage(bot, contact, member, content):
    insertData(contact, member, content)
