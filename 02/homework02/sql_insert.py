# encoding: utf-8
#!/usr/bin/python

import MySQLdb as mysql

# create db connect
db = mysql.connect(host="localhost", user="testuser", passwd="test123", db="testdb")

# create cursor
cursor = db.cursor()

sql = """insert into employee (first_name, 
    last_name, age, sex, income) 
    values ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    # execute the sql
    cursor.execute(sql)
    # commit the executed result
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# close db connect
db.close()