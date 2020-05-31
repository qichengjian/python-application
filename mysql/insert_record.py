import pymysql as pm

host = 'localhost'
user = 'root'
password = '123456'
dbname = 'test-python'

try:
    db = pm.connect(host, user, password, dbname)
    cursor = db.cursor()##获取数据库操作游标
    sql = 'insert into student(name, email, age) value (%s, %s, %s)'
    value = ('Smith', 'smith@qq.com', 19)

    cursor.execute(sql, value)
    db.commit()
    print("表数据插入成功！")
except pm.Error as e:
    print("表数据插入失败：" + str(e))
    db.rollback()

db.close()
