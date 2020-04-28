from mysql.connector import connect

db = connect(host='localhost', user='root', passwd='', database='python_db')

cursor = db.cursor()

sql = "update students set height = 5 , names = 'Sheila Nangila' , gender = 'female' where id = 1"

cursor.execute(sql)

db.commit()