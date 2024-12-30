from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/register")
def home():
    return "Register"

@app.route("/Login")
def home():
    return "Login"

@app.route("/getBooks")
def home():
    return "Hello, World!"

@app.route("/purchase")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()