import pymysql

db = pymysql.connect(host='127.0.0.1', user='user', password='password', database='test_db')
cursor = db.cursor()
sql = 'select * from test_table'
cursor.execute(sql)

# fetchone() 查询一条数据
rows = cursor.fetchall()
print('rows', rows)

for row in rows:
    print(row)
    print('id=%s, a=%s, b=%s' % (row[0], row[1], row[2]))

db.close()