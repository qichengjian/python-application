import pymysql as pm

host = 'localhost'
user = 'root'
password = '123456'
dbname = 'test-python'

try:
    db = pm.connect(host, user, password, dbname)
    cursor = db.cursor()##获取数据库操作游标
    sql = 'select * from student'
    cursor.execute(sql)

    result = cursor.fetchall()
    for row in result:
        print(row)
        print("name:%s, emal:%s, age:%s"%(row[0], row[1], row[2]))
    print("数据查询成功！")
except pm.Error as e:
    print("数据查询失败：" + str(e))
    db.rollback()

db.close()
