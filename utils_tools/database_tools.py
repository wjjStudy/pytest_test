# coding:utf-8

import pymysql


def fetch_all(conn, sql):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute() 方法执行 SQL 查询
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    return results
