from mysql.connector import connect

db = connect(host='localhost', user='root', passwd='', database='python_db')

cursor = db.cursor()

sql = "INSERT INTO `students` values(null,'Shishi Nangs' , 'sheilanangila@gmail.com' , 'female' , 7 , '1998-08-05') "

cursor.execute(sql)

db.commit()