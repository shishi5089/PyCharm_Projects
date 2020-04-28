from mysql.connector import connect

db = connect(host='localhost', user='root', passwd='', database='python_db')

cursor = db.cursor()

sql = "select * from students where id=50"

cursor.execute(sql)

data = cursor.fetchone()

print(data)

print(data[0],data[1] , data[2])

print(data[4])
