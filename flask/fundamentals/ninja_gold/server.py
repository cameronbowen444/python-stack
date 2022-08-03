from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route('/')
def ninja():
    gold = 0
    session['gold'] = gold
    if 'count' in session:
        session['count'] += gold
    return render_template("ninja_gold.html", gold=gold)


@app.route('/process', methods=['POST'])
def process():
    if request.form['find'] == 'farm':
        session['farm'] = request.form['find']
        session['farm'] = random.randint(10,20)
    elif request.form['find'] == 'cave':
        session['cave'] = request.form['find']
        session['cave'] = random.randint(5,10)
    elif request.form['find'] == 'house':
        session['house'] = request.form['find']
        session['house'] = random.randint(2,5)
    elif request.form['find'] == 'casino':
        session['casino'] = request.form['find']
        session['casino'] = random.randint(0,50)
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)


