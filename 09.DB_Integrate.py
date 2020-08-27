# Scenario:- for installation and start flask server
from flask import Flask, render_template, request
from db_module.TestData import TestData
from db_module.DataBaseFile import DataBaseFile


# Create object
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def loginpage():
    alert = ""
    if request.method == "POST":
        uname = request.form.get("USERNAME")                        #request.form["USERNAME"]
        pwd = request.form.get("PASSWORD")

        if uname == "admin" and pwd =="password":
            return render_template("home.html")
        else:
            alert = "invalid Credentials"
            return render_template("Login.html", alert = alert)
    return render_template('Login.html', alert = alert)

    # '<a href="/registration" >REGISTRATION</a>'


@app.route('/home')
def homepage():
    return render_template("home.html")


@app.route('/registration', methods = ["GET", "POST"])
def registration():
    if request.method == "POST":
        fname = request.form.get('firstName')
        lname = request.form.get('lastName')
        email = request.form.get('email')
        pwd = request.form.get('password')
        print(fname, lname, email, pwd)
        data = TestData(fname= fname, lname= lname, email= email, pwd= pwd)
        con = db.get_connection()
        db.create_table(con, 'table_data')
        db.insert_record(con, data, 'table_data')
        db.close_connection(con)
        return render_template('registration.html')
    return render_template("registration.html")


# Run the Server in Debug
if __name__ == "__main__":
    db = DataBaseFile('db_module/TestDataB.db')
    app.run(debug=True, port=5103)
