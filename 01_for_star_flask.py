# Scenario:- for installation and start flask server
from flask import Flask

# Create object
app = Flask(__name__)


# Run the Server in Debug
if __name__ == "__main__":
    app.run(debug=True)
