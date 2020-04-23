import pymysql,sys

host = "192.168.21.21"
port = "3306"
username = "root"
password = "123456"
db_name = "python" 

db = pymysql.connect(host=host, user=username, password=password, charset='utf8')

cursor = db.cursor()

#cursor.execute("create database test character set utf8;")

cursor.execute("use test;")

#cursor.execute("create table test_tab(id int,name char(20))character set utf8;")


sql = "insert into test_tab(id,name) values(%s,%s);"

count = 0
while True:
    sql_insert = 'insert into test_tab(id,name) values(%s,%s);'
    ID = input('请输入id：')
    if not ID:
        break
    name = input('请输入名字：')
    try:
        cursor.execute(sql_insert, [int(ID), name])
        count += 1
        db.commit()
        print('添加第%d条记录' % count, int(ID), name)
    except Exception as e:
        print('出错回滚完成', e)
        db.rollback()
        cursor.close()
        db.close()
        sys.exit()
del count

print("test git")
