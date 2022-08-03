from flask_app import app 
from flask import render_template, redirect, request
from flask_app.models import theclass
from flask_app.models import student

@app.route('/')
def index():
    return redirect('/classes')

@app.route('/classes')
def classes():
    return render_template('classes.html', classes=theclass.Theclass.get_all())

# @app.route('/addclass', methods=['POST'])
# def addnew():
#     theclass.Theclass.save(request.form)
#     return redirect('/')

@app.route('/classes/show/<int:id>')
def showclasses(id):
    data = {
        "id" : id
    }
    return render_template('showclasses.html',students=student.Student.get_all_s(), classes=theclass.Theclass.get_class_with_students(data))

@app.route('/addclass', methods=['POST'])
def enrolling():
    theclass.Theclass.add_class_to_student(request.form)
    return redirect(f"/classes/show/{request.form['class_id']}")
