from flask import Flask, render_template, request, redirect, flash
import re
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    print request.form
    err = False
    if len(request.form["first_name"]) < 1:
        flash("First Name cannot be blank!")
        err = True
    elif not request.form["first_name"].isalpha():
        flash("First Name must only contain letters!")
        err = True

    if len(request.form["last_name"]) < 1:
        flash("Last Name cannot be blank!")
        err = True
    elif not request.form["last_name"].isalpha():
        flash("Last Name must only contain letters!")
        err = True

    if len(request.form["email"]) < 1:
        flash("Email cannot be blank!")
        err = True
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email address!")
        err = True

    lower_error = re.search(r'[a-z]', request.form["password"]) is None
    upper_error = re.search(r'[A-Z]', request.form["password"]) is None
    num_error = re.search(r'[0-9]', request.form["password"]) is None

    if len(request.form["password"]) < 8:
        flash("Password must contain at least 8 characters!")
        err = True
    elif lower_error or upper_error or num_error:
        flash("Password must contain at least 1 lower case letter, 1 capital letter and 1 number!")
        err = True
    elif not request.form["password"] == request.form["confirm_password"]:
        flash("Passwords must match!")
        err = True

    if not err:
        flash("Thanks for submitting your information!")
    return redirect('/')

app.run(debug=True)
