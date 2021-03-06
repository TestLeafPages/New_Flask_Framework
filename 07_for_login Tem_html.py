# Scenario:- for installation and start flask server
from flask import Flask, render_template

# Create object
app = Flask(__name__)


@app.route('/')
def loginpage():
    return render_template('Login.html')

    # '<a href="/registration" >REGISTRATION</a>'


@app.route('/<name>')
def homepage(name):
    return f"hello {name}, Actually i'm home page"


@app.route('/registration')
def registration():
    return "im from registration Page"


# Run the Server in Debug
if __name__ == "__main__":
    app.run(debug=True, port=5010)
