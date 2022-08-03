from flask import Flask, render_template

pro = Flask(__name__)

@pro.route('/')
def checkers():
    return render_template("checkers.html",x=8,y=8,box1c="red",box2c="black")

@pro.route('/<int:y>')
def checkersy(y):
    return render_template("checkers.html",x=8,y=y,box1c="red",box2c="black")

@pro.route('/<int:y>/<int:x>')
def checkersyx(y,x):
    return render_template("checkers.html",x=x,y=y,box1c="red",box2c="black")

@pro.route('/<int:y>/<int:x>/<string:box1c>')
def checkerscol1(y,x,box1c):
    return render_template("checkers.html",x=x,y=y,box1c=box1c,box2c="black")

@pro.route('/<int:y>/<int:x>/<string:box1c>/<string:box2c>')
def checkerscol2(y,x,box1c,box2c):
    return render_template("checkers.html",x=x,y=y,box1c=box1c,box2c=box2c)

if __name__ == "__main__":
    pro.run(debug=True)
