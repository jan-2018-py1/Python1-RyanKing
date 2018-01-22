import random
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "activities" not in session:
        session["activities"] = ""
    return render_template("index.html")

@app.route('/process_money', methods=["POST"])
def process_money():
    if request.form["building"] == "farm":
        new_gold = random.randint(10, 20)
        session["gold"] += new_gold
        session["activities"] += "Earned {} gold from the farm!\n".format(new_gold)
    elif request.form["building"] == "cave":
        new_gold = random.randint(5, 10)
        session["gold"] += new_gold
        session["activities"] += "Earned {} gold from the cave!\n".format(new_gold)
    elif request.form["building"] == "house":
        new_gold = random.randint(2, 5)
        session["gold"] += new_gold
        session["activities"] += "Earned {} gold from the house!\n".format(new_gold)
    elif request.form["building"] == "casino":
        new_gold = random.randint(-50, 50)
        session["gold"] += new_gold
        if int(session["gold"]) < 0:
            session["gold"] = 0
        if new_gold < 0:
            session["activities"] += "Entered a casino and lost {} gold...ouch!\n".format(abs(new_gold))
        else:
            session["activities"] += "Entered a casino and won {} gold...yay!\n".format(new_gold)

    return render_template("index.html")

app.run(debug=True)
