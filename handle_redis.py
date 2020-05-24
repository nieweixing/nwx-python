#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   handle_redis.py
@Time    :   2020/05/11 15:05:15
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   连接redis操作
'''

# here put the import lib

import redis

#docker运行redis集群
#docker run -p 7000:7000 -p 7001:7001 -p 7002:7002 -p 7003:7003 -p 7004:7004 -p 7005:7005 -v /data/redis:/data tommy351/redis-cluster:4.0 

#连接redis
r = redis.Redis(host='192.168.21.21', port=6379, decode_responses=True)  
#print(r.info())

#set添加元素
r.sadd("ruyi-api:security:black-list:prod:appkey","3ecd870c-f628-4c4e-8d3d-028aeb0f9a43","3b01b176-5135-45d4-a2cb-52d22fdeacef")
#set删除元素
r.srem("ruyi-api:security:black-list:prod:appkey","3ecd870c-f628-4c4e-8d3d-028aeb0f9a43")
#查看某个set集合中的所有元素
print(r.smembers("ruyi-api:security:black-list:prod:appkey"))
#sismember：判断元素是否在集合中
print(r.sismember("ruyi-api:security:black-list:prod:appkey","3b01b176-5135-45d4-a2cb-52d22fdeacef"))


"""
string的命令操作

set(name, value, ex=None, px=None, nx=False, xx=False)
在 Redis 中设置值，默认，不存在则创建，存在则修改。
参数：
ex - 过期时间（秒）
px - 过期时间（毫秒）
nx - 如果设置为True，则只有name不存在时，当前set操作才执行
xx - 如果设置为True，则只有name存在时，当前set操作才执行
"""
r.set('food', 'mutton', ex=3)    # key是"food" value是"mutton" 将键值对存入redis缓存
print(r.get('food'))  # mutton 取出键food对应的值


"""
hset(name, key, value)
name对应的hash中设置一个键值对（不存在，则创建；否则，修改）
参数：
name - redis的name
key - name对应的hash中的key
value - name对应的hash中的value
注：hsetnx(name, key, value) 当name对应的hash中不存在当前key时则创建（相当于添加）
"""
r.hset("hash1", "k1", "v1")
r.hset("hash1", "k2", "v2")
print(r.hkeys("hash1")) # 取hash中所有的key
print(r.hget("hash1", "k1"))    # 单个取hash的key对应的值
print(r.hmget("hash1", "k1", "k2")) # 多个取hash的key对应的值
r.hsetnx("hash1", "k2", "v3") # 只能新建
print(r.hget("hash1", "k2"))
