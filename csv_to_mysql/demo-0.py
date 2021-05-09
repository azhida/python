import pandas as pd
import numpy as np
import pymysql

# 分块读取 csv文件数据

file_path = "test_table.csv"
table_name = "test_table"

chunksize = 2

count = 1

# 创建数据库连接
con = pymysql.connect(
    user='user',
    password='password',
    db='test_db',
    host='127.0.0.1'
)
con.set_charset('utf8')
cur = con.cursor()
cur.execute('set names utf8')
cur.execute('set character_set_connection=utf8;')

for df in pd.read_csv(file_path, chunksize=chunksize):
    # print('count: ', count, df)
    print('执行开始 count : ', count)
    count += 1

    # 将 表中所有为 null的数据 标记为 None_Null
    df = df.astype(object).where(pd.notnull(df), 'None_Null')

    # for index, row in df.iterrows():
        # print(index, row)

    # 数据表字段
    select_colunm = [
        'id',
        'name',
        'remark',
        'created_at',
        'updated_at',
    ]
    select_colunm = str(tuple(select_colunm))
    select_colunm = select_colunm.replace("'", '`')
    print('select_colunm', select_colunm)

    # 循环每一行的数据，并 将每一行 由数组 转为 字符串
    insert_data = [tuple(n) for n in df.values]
    print(97, insert_data)
    # 将所有行 由数组 转为 字符串
    insert_data = tuple(insert_data)
    print(96, insert_data)
    insert_data = str(insert_data)
    # 替换 NULL 值
    insert_data = insert_data.replace("'None_Null'", 'null')
    # 替换多余的 括号()
    insert_data = insert_data.replace("((", '(')
    insert_data = insert_data.replace("))", ')')
    insert_data = insert_data.replace("),)", ')')
    print(95, insert_data)

    # 拼接sql
    insert_sql = 'insert into `{}` {} values {}' . format(table_name, select_colunm, insert_data)
    print(90, insert_sql)

    # exit('stop')

    cur.execute(insert_sql)
    con.commit()

    print('执行结束')

    # break
    # x=row['djxh']
    # y=row[1]
    # print(index,x,y)



