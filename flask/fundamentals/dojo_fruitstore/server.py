from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    strawberry = request.form['strawberry']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    fruits = int(strawberry) + int(raspberry) + int(strawberry)
    full_name = f"{first_name} {last_name}"
    print(f" Charging {full_name} for {fruits} fruits!")
    return render_template("checkout.html",apple=apple,raspberry=raspberry,strawberry=strawberry,first_name=first_name,last_name=last_name,student_id=student_id)


@app.route('/fruits', methods=['GET', 'POST'])
def fruits():

    return render_template("fruits.html")


if __name__=="__main__":
    app.run(debug=True)