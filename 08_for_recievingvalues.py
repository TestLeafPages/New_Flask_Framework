# Scenario:- for installation and start flask server
from flask import Flask, render_template, request

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


@app.route('/registration')
def registration():
    return render_template("registration.html")


# Run the Server in Debug
if __name__ == "__main__":
    app.run(debug=True, port=5015)
