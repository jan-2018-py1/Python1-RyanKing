from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriends')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', all_friends=friends)

@app.route('/add', methods=["POST"])
def add():
    new_friend = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    query = "INSERT INTO friends (first_name, last_name, age, friend_since) VALUES (:first_name, :last_name, :age, now());"
    mysql.query_db(query, new_friend)
    return redirect('/')

app.run(debug=True)
