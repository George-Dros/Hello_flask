from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/Test")
def say_bye():
    return "<a>Test!</a>"

if __name__ == "__main__":
    app.run()