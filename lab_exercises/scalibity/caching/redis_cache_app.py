from flask import Flask
from flask_redis import FlaskRedis
import time


app = Flask(__name__)
app.config['REDIS_URL'] = "redis://localhost:6379/0"
redis_client = FlaskRedis(app)


@app.route("/")
def home():
    cached_result = redis_client.get("home_result")
    if cached_result:
        return cached_result.decode("utf-8")
    else:
        time.sleep(2)  # Simulating a slow database query
        result = "Cached result"
        redis_client.set("home_result", result, ex=30)  # Cache for 30 seconds
        return result

if __name__ == "__main__":
    app.run()