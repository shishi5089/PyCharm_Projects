from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/team/sales')
def teams():
    members = ['Sheila', 'Malea', 'Arnold', 'Mary', 'Felicia']
    name = 'Shishi'
    return render_template('teams.html', members=members, name=name)


@app.errorhandler(404)
def error(e):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)


