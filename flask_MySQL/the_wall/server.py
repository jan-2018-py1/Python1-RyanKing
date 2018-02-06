from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import md5, re
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, "the_wall")

@app.route('/')
def index():
    if "id" in session:
        return redirect('/wall')
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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :password, now(), now())"
        data = {
            "first": first_name,
            "last": last_name,
            "email": email,
            "password": md5.new(password).hexdigest()
        }
        session["id"] = mysql.query_db(query, data)
        return redirect('/wall')

@app.route('/login', methods=["POST"])
def login():
    email = request.form["email"]
    password = md5.new(request.form["password"]).hexdigest()
    query = "SELECT * FROM users WHERE users.email = :email AND users.password = password"
    data = {"email": email, "password": password}
    user = mysql.query_db(query, data)
    if len(user) == 0:
        flash("User doesn't exist!")
        return redirect('/')
    else:
        user = user[0]
        session["id"] = user["id"]
        return redirect('/wall')

@app.route('/post', methods=["POST"])
def post():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, now(), now())"
    data = {
        "user_id": session["id"],
        "message": request.form["post"]
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment', methods=["POST"])
def comment():
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, now(), now())"
    data = {
        "message_id": request.form["post_id"],
        "user_id": session["id"],
        "comment": request.form["comment"]
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall')
def wall():
    if "id" not in session:
        return redirect('/')

    user_name = mysql.query_db("SELECT first_name FROM users WHERE id = :id", {"id": session["id"]})

    message_query = "SELECT users.id AS poster_id, users.first_name AS poster_first_name, users.last_name AS poster_last_name, messages.message AS post, messages.id AS post_id, DATE_FORMAT(messages.created_at, '%m/%d/%Y') AS post_date FROM users JOIN messages ON users.id = messages.user_id ORDER BY post_id DESC"
    all_messages = mysql.query_db(message_query)

    comment_query = "SELECT users.id AS commenter_id, users.first_name AS commenter_first_name, users.last_name AS commenter_last_name, messages.id AS post_id, comments.id AS comment_id, comments.comment AS comment, DATE_FORMAT(comments.created_at, '%m/%d/%Y') AS comment_date FROM comments JOIN users ON comments.user_id = users.id JOIN messages ON comments.message_id = messages.id ORDER BY comment_id"
    all_comments = mysql.query_db(comment_query)

    return render_template("wall.html", first_name=user_name[0]["first_name"], all_messages=all_messages, all_comments=all_comments)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
