from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "aaaaaa"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if len(request.form["name"]) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    if len(request.form["comments"]) < 1:
        flash("Comments cannot be empty!")
        return redirect('/')
    elif len(request.form["comments"]) > 120:
        flash("Comments too long!")
        return redirect('/')

    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comments = request.form["comments"]
    return render_template("result.html", name=name, location=location, language=language, comments=comments)

app.run(debug=True)
