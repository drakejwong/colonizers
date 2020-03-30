import flask

app = flask.Flask(__name__)

@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Let's Colonize!")

app.run(debug=True)