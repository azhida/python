import pymysql

db = pymysql.connect(host='127.0.0.1', user='user', password='password', database='test_db')
cursor = db.cursor()

sql = 'select *  from test_table'
cursor.execute(sql)
rows = cursor.fetchall()
print('rows_1', format(rows))

try:
    id = 3
    sql = 'delete from test_table where id = %d' % id
    print(sql)
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)

sql = 'select *  from test_table'
cursor.execute(sql)
rows = cursor.fetchall()
print('rows_2', format(rows))

db.close()