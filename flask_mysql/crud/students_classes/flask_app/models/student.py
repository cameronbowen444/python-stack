from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import theclass

class Student:
    db = "students_classes"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.classes = []

    @classmethod 
    def get_all_s(cls):
        query = "SELECT * FROM students;"
        results = connectToMySQL(cls.db).query_db(query)

        students = []
        for student in results:
            students.append(cls(student))
        return students


    @classmethod
    def get_student_with_classes(cls, data):
        query = "SELECT * FROM students LEFT JOIN enrollment ON enrollment.student_id = students.id LEFT JOIN classes ON enrollment.class_id = classes.id WHERE student.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)

        student = cls(results[0])
        for row in results:
            class_data = {
                "id" : row['classes.id'],
                "name" : row['name'],
                "units" : row['units'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            student.classes.append(theclass.Theclass(class_data))
        return student

    @classmethod
    def add(cls, data):
        query = "INSERT INTO students (first_name, last_name, age, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod 
    def get_student_id(cls, data):
        query = "SELECT * FROM students WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results[0]