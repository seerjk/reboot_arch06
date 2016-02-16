# encoding: utf-8
#!/usr/bin/python

import MySQLdb as mysql

db = mysql.connect(host="localhost", user="testuser", passwd="test123", db="testdb")

cursor = db.cursor()

sql = "drop table if exists employee"
cursor.execute(sql)

sql = """
    create table employee (
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float
    )
"""
cursor.execute(sql)

sql = "desc employee"
cursor.execute(sql)

# res = cursor.fetchall()
# print res

db.close()