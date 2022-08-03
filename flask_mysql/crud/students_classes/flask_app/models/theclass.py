from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import student

class Theclass:
    db = "students_classes"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.units = data['units']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.students = []

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM classes;"
        results = connectToMySQL(cls.db).query_db(query)

        classes = []
        for c in results:
            classes.append(cls(c))
        return classes

    @classmethod
    def get_class_with_students(cls, data):
        query = "SELECT * FROM classes LEFT JOIN enrollment ON enrollment.class_id = classes.id LEFT JOIN students ON enrollment.student_id = students.id WHERE classes.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)

        classes = cls(results[0])
        for row in results:
            student_data = {
                "id" : row['students.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            classes.students.append(student.Student(student_data))
        return classes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO classes (name, units, created_at, updated_at) VALUES (%(name)s, %(units)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)


    @classmethod
    def add_class_to_student(cls, data):
        query = "INSERT INTO enrollment (student_id, class_id) VALUES (%(student_id)s, %(class_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)