import pymongo
import json

client = pymongo.MongoClient(host='192.168.30.31',port=27017)

#创建数据库
mydb = client["mydb"]
#创建集合，也就是表 
mycol = mydb["sitesssss"]
mydict = { "name": "RUNOOB","alexa": "10000","url": "https://www.runoob.com" }
mycol.insert_one(mydict)


mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
mycol.insert_many(mylist)

for j in mydb.list_collection_names():
  print(j)

dbs = client.list_database_names()

for i in dbs:
  print(i)



mongostatus =  client.server_info()



#print(json.dumps(mongostatus,indent=1))

client.close()
