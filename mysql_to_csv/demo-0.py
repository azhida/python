import pandas as pd
import pymysql

db = pymysql.connect(host='127.0.0.1', user='user', password='password', database='test_db')
cursor = db.cursor()
sql = 'select * from test_table'
cursor.execute(sql)

# 获取字段信息
col_result = cursor.description
print('col_result', col_result)

# 获取所有查询结果
rows = cursor.fetchall()
print('rows', rows)

db.close()

# 以列表形式保存字段名
columns = []
for i in range(0, len(col_result)):
    columns.append(col_result[i][0])
print('columns', columns)

# 整理查询结果，转为 列表list
data = list(map(list, rows))
print('rows', rows)
print('data', data)

# 参数encoding="utf_8_sig"编码后，可以防止写入csv的中文出现乱码
# df.to_csv("./test.csv", encoding="utf_8_sig")

df = pd.DataFrame(data=data, columns=columns)  # mysql查询的结果为元组，需要转换为列表
df.to_csv('csvs/demo-0.csv', index=None, encoding="utf_8_sig")


