#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   query_bot_account_info.py
@Time    :   2020/05/09 17:08:13
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   niewx@ruyi.ai
@Desc    :   Query user information based on bot app_id
'''

# here put the import lib

import pymongo
import json
import pymysql
import sys

#Query appDeveloperId from mongo

app_id = sys.argv[1]
client = pymongo.MongoClient(host='10.0.1.153',port=27017)
db = client.db_ruyi
#选在集合
collection = db.appModel
result = collection.find_one({"_id":app_id})
new_result = json.dumps(result)
data2 = json.loads(new_result)
deploy_id = data2.get("appDeveloperId")


#Query user information from mysql based on appDeveloperId

host = "ai-production-mysql-bot.cfyipcsxzevb.rds.cn-northwest-1.amazonaws.com.cn"
port = "3306"
username = "cas_server"
password = "secret_cas"
db_name = "microservice_ruyisso_cas"
db = pymysql.connect(host=host, user=username, password=password, charset='utf8')
cursor = db.cursor()
cursor.execute("use {}".format(db_name))
sql = "SELECT * from users where id = '{}';".format(deploy_id)
count_info = cursor.execute(sql)
result_data=cursor.fetchall()
print("bot账户信息如下:")
print("deveploper_id: {}".format(result_data[0][0]).encode('utf8'))
print("email: {}".format(result_data[0][3]).encode('utf8'))
print("phone_number: {}".format(result_data[0][4]).encode('utf8'))
