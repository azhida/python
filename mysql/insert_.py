import pymysql

db = pymysql.connect(host='127.0.0.1', user='user', password='password', database='test_db')
cursor = db.cursor()

try:
    sql = 'insert into test_table (a, b) values (2, 2), (3, 3)'
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)

sql = 'select *  from test_table'
cursor.execute(sql)
rows = cursor.fetchall()
print('rows', rows)

for row in rows:
    print(row)
    print('id=%s, a=%s, b=%s' % (row[0], row[1], row[2]))

db.close()