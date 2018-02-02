from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app, "email_validation")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    new_email = request.form["email"]
    if not EMAIL_REGEX.match(new_email):
        flash("Email is not valid!")
        return redirect('/')

    query_add = "INSERT INTO emails (email, created_at) VALUES (:email, now())"
    data = {"email": new_email}
    mysql.query_db(query_add, data)

    flash("The email address you entered (" + new_email + ") is a VALID email address! Thank you!")
    email_list = mysql.query_db("SELECT * FROM emails")
    return render_template("success.html", email_list=email_list)

app.run(debug=True)
