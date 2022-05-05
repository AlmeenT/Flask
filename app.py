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
        user_response = request.form['Word']
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute('select meaning from word where word =%s', (user_response))
        rv = cur.fetchall()
        if(len(rv) > 0):
            user_response = rv[0]['meaning']
        else:
            user_response = 'word cannot ne found in this dictionary. Please try another word'
    return render_template('home.html', user_response = user_response )

@app.route('/dashboard')
def dashboard():
    conn = mysql.get_db()
    cur = conn.cursor()
    cur.execute('select * from word')
    rv = cur.fetchall()
    for item in rv:
        print(item)
    return render_template('dashboard.html', words = [])


if __name__ == "__main__":
    app.run(debug=True)