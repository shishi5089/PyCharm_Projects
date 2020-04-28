from mysql.connector import connect

db = connect(host='localhost', user='root', passwd='', database='python_db')

cursor = db.cursor()
# sql injection
data = ('', 'Shishi Nangs', 'sheilanangila@gmail.com', 'female', 7, '1998-08-05')

sql = "INSERT INTO `students` values(%s ,%s ,%s ,%s , %s , %s) "

cursor.execute(sql , data)
# dynamic binding - mitigates sql injection
db.commit()

# flask
