

from sqlite3 import connect as con


def inisert(sql, title, author, kind, intro, content):
    conn = con(r'data/poem.db')  # 连接到db文件
    c = conn.cursor()  # 创建一个Cursor
    c.execute(sql % (title, author, kind, intro, content))  # 执行sql语句
    c.close()  # 关闭Cursor
    conn.commit()  # 提交操作
    conn.close()  # 提交操作


def check(sql):
    lis = []
    conn = con(r'data/poem.db')  # 连接到db文件
    c = conn.cursor()  # 创建一个Cursor
    c.execute(sql)  # 执行sql语句
    for row in c.fetchall():
        lis.append(row)  # 查询到的元组添加到列表中
    c.close()  # 关闭Cursor
    conn.close()  # 提交操作
    tup = tuple(lis)  # 为了兼容之前的接口将列表转换为元组
    return tup
