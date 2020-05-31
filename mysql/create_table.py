import pymysql as pm

host = 'localhost'
user = 'root'
password = '123456'
dbname = 'test-python'

try:
    db = pm.connect(host, user, password, dbname)
    cursor = db.cursor()##获取数据库操作游标
    cursor.execute("drop table if exists student")
    sql = 'create table student(name char(20) not null, email char(20), age int )'
    cursor.execute(sql)
    print("数据库表创建成功！")
except pm.Error as e:
    print("数据库表创建失败：" + str(e))
