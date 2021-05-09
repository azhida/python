import pandas as pd
import numpy as np
import pymysql

file_path = "test_table.csv"
table_name = "test_table"

try:
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

    # 创建数据表 字段
    create_colunm = [
        '`id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT',
        '`name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL',
        '`remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL',
        '`created_at` datetime(0) NULL DEFAULT NULL',
        '`updated_at` datetime(0) NULL DEFAULT NULL',
        'PRIMARY KEY(`id`) USING BTREE',
    ]
    create_colunm = str(tuple(create_colunm))
    create_colunm = create_colunm.replace("'", '')

    create_table_sql = 'create table if not exists `{}` {} default charset=utf8' . format(table_name, create_colunm)
    print(create_table_sql)
    cur.execute(create_table_sql)

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

    # 读取 csv文件
    df = pd.read_csv(file_path)
    # 将 表中所有为 null的数据 标记为 None_Null
    df = df.astype(object).where(pd.notnull(df), 'None_Null')

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
    print(95, insert_data)

    # 拼接sql
    insert_sql = 'insert into `{}` {} values {}' . format(table_name, select_colunm, insert_data)
    print(90, insert_sql)

    cur.execute(insert_sql)
    con.commit()

    print('执行结束')

except Exception as e:
    print(e)

finally:
    cur.close()
    con.close()


