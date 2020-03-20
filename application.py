from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello, World! V.0.1"

if __name__ == "__main__":
    application.run()
