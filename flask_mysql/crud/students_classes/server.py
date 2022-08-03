from flask_app import app 
from flask_app.controllers import students
from flask_app.controllers import classes


if __name__=="__main__":
    app.run(debug=True)