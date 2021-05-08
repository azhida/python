import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', user='user', password='password', database='db_name')

# 创建一个游标对象 cursor
cursor = db.cursor()

# 执行sql查询
sql = 'SELECT version()'
cursor.execute(sql)

# 获取单条数据
data = cursor.fetchone()
print('mysql版本：', data)
print('mysql版本：%s' % data)

# 关闭数据库连接
db.close()