import pymysql

db = pymysql.connect(host='127.0.0.1', user='user', password='password', database='test_db')
cursor = db.cursor()

sql = 'select *  from test_table'
cursor.execute(sql)
rows = cursor.fetchall()
print('rows_1', format(rows))

try:
    id = 4
    a = 'aaa3c'
    sql = 'update test_table set a = "%s" where id = %d' % (a, id)
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