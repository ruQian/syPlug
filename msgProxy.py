# -*- coding: utf-8 -*-

import traceback
import uuid
import time
import pandas as pd
from pymysqlpool import ConnectionPool
config = {
 'pool_name': 'qqMsgDBPool',
 'host': '47.93.240.110',
 'port': 3306,
 'user': 'root',
 'password': 'a1b2c3',
 'database': 'sydb'
}
def connection_pool():
	# Return a connection pool instance
	pool = ConnectionPool(**config)
	pool.connect()
	return pool
	
try:
	conPool = connection_pool()
except:
	traceback.print_exc()
def insertData(contact, member, content):
    try:
#ctype/qq/uin/nick/mark/card/name    
        print("contact.ctype-- %s" % (contact.ctype))
        print("contact.qq-- %s" % (contact.qq))
        print("contact.uin-- %s" % (contact.uin))
        print("contact.nick-- %s" % (contact.nick))
        print("contact.mark-- %s" % (contact.mark))
        #print("contact.card-- %s" % (contact.card))
        print("contact.name-- %s" % (contact.name))
        print("member-- %s" % (member))
        print("content-- %s" % (content))
        if(contact.ctype == 'group'):
            with conPool.connection(autocommit=True) as conn:
                strUid = str(uuid.uuid1())
                tiInt = int(time.time())
                conn.cursor().execute('INSERT INTO qqGroupMsgPool \
                (guid, msgTime, rawMsg, groupNick, groupName,groupID,groupMember,groupMemberID) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', \
                    (strUid,tiInt,content.encode('utf-8'),\
                    contact.nick.encode('utf-8'),contact.name.encode('utf-8'),contact.qq.encode('utf-8'),\
                    str(member).encode('utf-8'),contact.uin.encode('utf-8')))
    except:
        traceback.print_exc()



def onQQMessage(bot, contact, member, content):
    insertData(contact, member, content)
