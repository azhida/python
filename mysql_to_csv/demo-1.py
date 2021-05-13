import pandas as pd
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='user', password='password', database='test_db')
cursor = conn.cursor()
sql = 'select * from test_table'

# 参数encoding="utf_8_sig"编码后，可以防止写入csv的中文出现乱码
df = pd.read_sql(sql, con=conn)
print(df.head())

df.to_csv('csvs/demo-1.csv', index=None, encoding="utf_8_sig")
conn.close()
