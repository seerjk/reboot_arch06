# encoding: utf-8
#!/usr/bin/env python

import MySQLdb as mysql

# 1.打开数据库连接
db = mysql.connect(host="localhost", user="testuser", passwd="test123", db="testdb")

# 2.使用cursor()方法获取操作游标
cursor = db.cursor()

# 3.使用execute()方法执行SQL语句
cursor.execute("select version()")

# 使用fetchone()方法，获取一条执行结果
data = cursor.fetchone()

print "Database version: %s" % data

# 4.关闭数据库连接
db.close()