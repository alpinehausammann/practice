from peewee import *

db = SqliteDatabase('students.db')


class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db
students = [
    {"andehausammann":101},
    {"ahouse":54},
    {"artie":15672},
    {"eric":20000},
    {"consuela":4500},
]


def add_students():
        for student in students:
            for username in student:
                try:
                    Student.create(username=username, points=student[username])
                except IntegrityError:
                    student_record = Student.get(username=username)
                    student_record.points = student[username]
                    student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("our top studnet right now is:{0.username}".format(top_student()))
