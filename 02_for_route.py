# Scenario:- for installation and start flask server
from flask import Flask

# Create object
app = Flask(__name__)


@app.route('/')
def loginpage():
    return "Hello all, Im building something with the help of flask"


@app.route('/home')
def homepage():
    return "im home page"




# Run the Server in Debug
app.run(debug=True)
