import pymysql as pm


host = 'localhost'
user = 'root'
password = '123456'
dbname = 'test-python'

try:
    db = pm.connect(host, user, password, dbname)
    print("数据库连接成功")
except pm.Error as e:
    print("数据库连接失败：" + str(e))
