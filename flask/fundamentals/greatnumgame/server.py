from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = 'camcambaby the secret is real'



@app.route('/')
def index():
    if "count" not in session:
        session['count'] = random.randint(1,100)
    return render_template("greatnumgame.html")

@app.route('/guess', methods=['POST'])
def guess_num():
    session['guess_num'] = int(request.form['guess_num'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
