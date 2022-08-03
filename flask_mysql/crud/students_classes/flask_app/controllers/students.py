from flask_app import app 
from flask import render_template, redirect, request
from flask_app.models import student
from flask_app.models import theclass

@app.route('/students')
def students():
    students=student.Student.get_all_s()
    return render_template('students.html',students=students)



@app.route('/students/show/<int:id>')
def showstudents(id):
    data = {
        "id" : id
    }
    return render_template('showstudents.html', classes=theclass.Theclass.get_all(), these_classes=student.Student.get_student_id(data))


@app.route('/addstudent', methods=['POST'])
def enrollement():
    theclass.Theclass.add_class_to_student(request.form)
    return redirect(f"/students/show/{request.form['student_id']}")