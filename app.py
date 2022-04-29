from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<firstname>/<lastname>')
def greet(firstname,lastname):
    name = f'{firstname}{lastname}'
    return render_template('greet.html', name= name)

if __name__ == "__main__":
    app.run(debug=True)