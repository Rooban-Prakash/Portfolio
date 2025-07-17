# test.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h2>Python server is up!</h2>"

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    message = request.form.get("message")
    print(f"Received: Name={name}, Message={message}")
    return f"Thanks {name}, your message was received!"

if __name__ == "__main__":
    app.run(debug=True)
