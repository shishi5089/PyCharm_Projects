from mysql.connector import connect

db = connect(host='localhost', user='root', passwd='', database='python_db')

cursor = db.cursor()

sql = "delete from students where names='Sheila Nangila'"

cursor.execute(sql)

db.commit()