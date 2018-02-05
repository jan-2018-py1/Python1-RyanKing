from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import md5, re
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, "logins")

@app.route('/')
def index():
    if "id" in session:
        return redirect('/success')
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def register():
    err = False
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    confirm = request.form["confirm"]

    if len(first_name) < 2:
        flash("First name must be at least 2 letters!")
        err = True
    if not first_name.isalpha():
        flash("First name must only contain letters!")
        err = True
    if len(last_name) < 2:
        flash("Last name must be at least 2 letters!")
        err = True
    if not last_name.isalpha():
        flash("Last name must only contain letters!")
        err = True
    if len(email) < 1:
        flash("Email address cannot be blank!")
        err = True
    if not EMAIL_REGEX.match(email):
        flash("Invalid Email Format!")
        err = True
    if len(password) < 8:
        flash("Password must be at least 8 characters!")
        err = True
    if password != confirm:
        flash("Passwords don't match!")
        err = True

    if err:
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first, :last, :email, :password)"
        data = {
            "first": first_name,
            "last": last_name,
            "email": email,
            "password": md5.new(password).hexdigest()
        }
        session["id"] = mysql.query_db(query, data)
        return redirect('/success')

@app.route('/login', methods=["POST"])
def login():
    email = request.form["email"]
    password = md5.new(request.form["password"]).hexdigest()
    query = "SELECT * FROM users WHERE users.email = :email AND users.password = password"
    data = {"email": email, "password": password}
    user = mysql.query_db(query, data)[0]
    if len(user) == 0:
        flash("User doesn't exist!")
        return redirect('/')
    else:
        session["id"] = user["id"]
        return redirect('/success')

@app.route('/success')
def success():
    if "id" in session:
        query = "SELECT first_name FROM users WHERE id = :id"
        data = {"id": session["id"]}
        user = mysql.query_db(query, data)[0]
        return render_template("success.html", first_name=user["first_name"])
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
