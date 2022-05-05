from flask import Flask, render_template, url_for, request
from flaskext.mysql import MySQL
import pymysql.cursors

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'dictionary'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ha1la3ma1ta'

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods = ['GET', 'POST'] )
def home():
    user_response = ''
    if request.method == 'POST':
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute('select meaning from word where word =%s', ('flask'))
        rv = cur.fetchall()
        user_response = request.form['Word']
    return render_template('home.html', user_response = user_response )

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)