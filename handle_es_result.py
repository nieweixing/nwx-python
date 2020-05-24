#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   handle_es_result.py
@Time    :   2020/05/09 17:09:41
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   One week statistics of bot traffic
'''

# here put the import lib
import json,os,io,sys,csv,time,codecs

#python3的写法
#import importlib,sys 
#importlib.reload(sys)

#python2的写法
#reload(sys)
#sys.setdefaultencoding( "utf-8" )


os.system("sh query_es.sh")

f = io.open("result.json", "r", encoding='utf-8')
result_str = json.load(f)
print(result_str)

result = result_str.get("aggregations").get("groud_by_app_name_100").get("buckets")
print(result)

number = 0


tag = time.strftime('%Y-%m-%d',time.localtime())
filename = "bot_week_report-{}.csv".format(tag)

week_result = io.open(filename, 'wb')
week_result.write(codecs.BOM_UTF8)
csv_writer = csv.writer(week_result)
csv_writer.writerow(["序号","bot名称","文档数量","类型数量"])

for i in result:
    name = i["key"]
    doc_count = str(i["doc_count"])
    type_count = str(i["type_count"].get("value"))
    print("{}:{} {} {}".format(number,name, doc_count,type_count))
    number+=1
    line_list = [number,name, doc_count,type_count]

    csv_writer.writerow(line_list)
    line_list[:] = []

week_result.close()
f.close()

upload_key = "aws s3 cp {} s3://kg-api-production".format(filename)
os.system(upload_key)

rm_csv_file = "rm -rf {}".format(filename)
os.system(rm_csv_file)

rm_result_file = "rm -rf result.json"
os.system(rm_result_file)