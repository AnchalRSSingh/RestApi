from flask import Flask,jsonify

todo = Flask(__name__)

students=[
    {
        'id':1,
        'name':'lion',
        'age':20
    },
    {
        'id': 2,
        'name': 'lion',
        'age': 20
    },
    {
        'id':3,
        'name':'lion',
        'age':20
    },
    {
        'id':4,
        'name':'lion',
        'age':20
    },
]

@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/student/get/<int:id>')
def get_student_by_id(id):
    print(id)
    for std in students:
        if std['id']==id:
           return jsonify(std)
        print(std)
    return "i will return student"


if __name__=='__main__':
    todo.run(
        debug=True
    )