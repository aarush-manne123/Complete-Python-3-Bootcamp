from flask import *
app = Flask(__name__)
@app.route("/")
def Index():
    return """
    <h1>Hello World</h1>
    <p>I made this website with python FLASK</p>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1472)
