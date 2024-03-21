import pymysql

conn = pymysql.connect(
    user='root',
    password='root',
    host='127.0.0.1',
    port=3307,
    database='msg'
)

cursor = conn.cursor()
cursor.execute('use msg')
cursor.execute('show table result')

result = cursor.fetchall()
print('查询到的结果',result)

cursor.close()
conn.close()

