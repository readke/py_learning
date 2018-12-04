import pymysql

db = pymysql.connect("pactera.com","root","java","test")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("database verion : %s" % data)

db.close()
