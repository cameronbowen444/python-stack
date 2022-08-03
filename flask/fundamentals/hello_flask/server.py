from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html",banana=banana, num=num)


@app.route('/play')
def play():
    return render_template("playground.html", num=3, color="lightblue")

@app.route('/play/<int:num>')
def playground(num):
    return render_template("playground.html",num=num, color="lightblue")

@app.route('/play/<int:num>/<color>')
def play_time(num,color):
    return render_template("playground.html",num=num, color=color)


@app.route('/lists')
def render_lists():
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30},
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



@app.route('/users/<username>/<id>')
def users(username,id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":
    app.run(debug=True)

