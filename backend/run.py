import flask

app = flask.Flask(__name__)

@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Let's Colonize!")

if __name__ == "__main__":
    app.run(debug=True)