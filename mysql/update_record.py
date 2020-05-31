import pymysql as pm

host = 'localhost'
user = 'root'
password = '123456'
dbname = 'test-python'

try:
    db = pm.connect(host, user, password, dbname)
    cursor = db.cursor()##获取数据库操作游标
    sql = 'update student set email=%s, age = %s where name = %s'
    value = ('11@qq.com', 111, 'Smith')
    cursor.execute(sql, value)
    db.commit()

    print("数据更新成功！")
except pm.Error as e:
    print("数据更新失败：" + str(e))
    db.rollback()

db.close()
