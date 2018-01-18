import random
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    session["compare"] = ""
    if "winner" not in session:
        session["winner"] = random.randrange(1, 101)
    if "guess" in session:
        if session["guess"] == session["winner"]:
            return render_template('win.html')
        elif session["guess"] < session["winner"]:
            session["compare"] = "Too Low!"
            return render_template("index.html")
        elif session["guess"] > session["winner"]:
            session["compare"] = "Too High!"
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    session["guess"] = int(request.form["user_guess"])
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop("winner")
    session.pop("guess")
    return render_template("index.html")

app.run(debug=True)
