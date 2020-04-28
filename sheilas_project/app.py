from flask import Flask, render_template, request, redirect, url_for, flash, session
from mysql.connector import connect

app = Flask(__name__)
db = connect(host='localhost', user='root', passwd='', database='sheila_project')
app.secret_key = 'ddnvdvndvndnlxnn'


@app.route('/')
def home():
    if session.get('id') == None:
        return redirect(url_for('login'))
    return render_template('home.html')


@app.route('/dogs')
def dogs():
    if session.get('id') == None:
        return redirect(url_for('login'))
    return render_template('dogs.html')


@app.route('/cats')
def cats():
    if session.get('id') == None:
        return redirect(url_for('login'))
    return render_template('cats.html')


@app.route('/about')
def about():
    if session.get('id') == None:
        return redirect(url_for('login'))
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/add_pet', methods=['POST', 'GET'])
def add_pet():
    if session.get('id') == None:
        return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('add_pet.html')
    else:
        print(request.form)
        animal_name = request.form["animal_name"]
        animal_type = request.form["animal_type"]
        age = request.form["age"]
        gender = request.form["gender"]
        category = request.form["category"]
        price = request.form["price"]

        print(animal_name, animal_type, age, gender, category, price)
        cursor = db.cursor()
        sql = "insert into animals values(null, %s, %s,%s,%s,%s,%s)"
        data = (animal_name, animal_type, age, gender, category, price)
        cursor.execute(sql, data)
        db.commit()
        flash("Added pet successfully ", "text-info")

    return render_template('add_pet.html')


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    # if session.get('id') == None:
    #     return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        print(request.form)
        user_name = request.form["user_name"]
        email = request.form["email"]
        password = request.form["password"]

        cursor = db.cursor()
        sql = "insert into users values(null, %s, %s,%s)"
        data = (user_name, email, password)
        cursor.execute(sql, data)
        db.commit()
        flash("Added user successfully", "text-info")

    return render_template('add_user.html')


@app.route('/animals')
def animals():
    if session.get('id') == None:
        return redirect(url_for('login'))
    sql = 'select * from animals'
    cursor = db.cursor()
    cursor.execute(sql)
    animals = cursor.fetchall()
    print(animals)
    # items = ['Sprays', 'Bracelets', 'Earrings', 'Necklaces', 'Shoes']
    return render_template('animals.html', animals=animals)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print(request.form)
        email = request.form["email"]
        password = request.form["password"]

        cursor = db.cursor()
        sql = "select * from users where email = %s and password = %s"
        data = (email, password)
        cursor.execute(sql, data)
        user = cursor.fetchone()
        print(user)
        if user == None:
            flash("Wrong username or password", "text-danger")
            return redirect(url_for('login'))
        else:
            session["user_name"] = user[1]
            session["email"] = user[2]
            session["id"] = user[0]
            flash("Logged in successfully", "text-info")
            return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/status/<id>')
def status(id):
    if session.get('id') is None:
        return redirect(url_for('login'))
    sql = 'delete from animals where id=%s'
    data = (id,)
    cursor = db.cursor()
    cursor.execute(sql, data)
    db.commit()
    flash("Purchased successfully", "text-danger")
    return redirect(url_for('animals'))


@app.route('/logout')
def logout():
    if session.get('id') == None:
        return redirect(url_for('login'))
    session.clear()
    flash("Logged out successfully", "text-info")
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
