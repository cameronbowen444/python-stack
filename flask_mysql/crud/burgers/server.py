from flask import render_template,redirect,request,session

from flask_app import app

from flask_app.models.burger import Burger
from flask_app.controllers import burgers




if __name__=="__main__":
    app.run(debug=True)