from flask_app import app
from flask_app.controllers import millionaires, incomes

if __name__=="__main__":
    app.run(debug=True)