from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def ninja_color(color):
    if color == "blue":
        img_url = "img/leonardo.jpg"
    elif color == "orange":
        img_url = "img/michelangelo.jpg"
    elif color == "red":
        img_url = "img/raphael.jpg"
    elif color == "purple":
        img_url = "img/donatello.jpg"
    else:
        img_url = "img/notapril.jpg"

    return render_template("color.html", img_url=img_url)

app.run(debug=True)
