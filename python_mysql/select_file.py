from mysql.connector import connect

db = connect(host='localhost', user='root', passwd='', database='python_db')

cursor = db.cursor()

sql = "select names , gender from students where names like  '%s' "

cursor.execute(sql)

data = cursor.fetchall()

print(data)

for item in data:
    print(item[0] , item[1])