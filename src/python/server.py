from flask import Flask, send_file
app = Flask(__name__)


@app.route("/")
def cat():
    return send_file("Cat_poster_1_wikipedia.jpg")


@app.route("/kittens.webm")
def kittens():
    return send_file("sweetheartkittens.webm", mimetype="video/webm")


@app.route("/kittens2.webm")
def kittens2():
    return send_file("maipmkittens.webm", mimetype="video/webm")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
