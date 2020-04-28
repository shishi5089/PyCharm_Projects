from mysql.connector import connect

db = connect(host='localhost', user='root', passwd='', database='python_db')

cursor = db.cursor()

sql = "select names , height from students where height < (SELECT AVG(height)FROM students)"

cursor.execute(sql)

data = cursor.fetchall()

print(data)

for item in data:
    print(item[0],item[1])