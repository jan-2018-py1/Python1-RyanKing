from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comments = request.form["comments"]
    return render_template("result.html", name=name, location=location, language=language, comments=comments)

app.run(debug=True)
