from flask import Flask
import time
app = Flask(__name__)

@app.route("/")
def home():
    time.sleep(2)
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5001")