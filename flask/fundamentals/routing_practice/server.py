from flask import Flask

pract = Flask(__name__)

@pract.route('/')
def hello_world():
    return f" Hello World"

@pract.route('/dojo')
def run_dojo():
    return f" Dojo!"

@pract.route('/say/<word>')
def say_something(word):
    return f" Hi {word}!"

@pract.route('/repeat/<string:word>/<int:num>')
def repeat(word,num):
    return f" Hello {word * num}"

if __name__=="__main__":
    pract.run(debug=True)
