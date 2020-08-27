from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def sampleJinja():
    lst = ['Item', 'Item', 'Item', 'Item']
    name = "Babu"
    type = 123
    return render_template("sample.html", name = name, type = lst)



if __name__ == "__main__":
    app.run(debug=True, port=5100)