# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.
from flask import Flask, render_template
from HW_3.models_03 import db, Student, Mark

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'University'


@app.route('/university/')
def get_library_list():
    university = Mark.query.all()
    context = {'university': university}
    return render_template('university.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('University OK ')


@app.cli.command("add-student")
def add_student():
    student = Student(first_name='Alex', last_name='Petrov', group='3', email='petroff@mail.ru')
    db.session.add(student)
    db.session.commit()
    print('Student OK!')


@app.cli.command("add-mark")
def add_mark():
    mark = Mark(subject_name='Chemy', mark=5, student_id=1)
    db.session.add(mark)
    db.session.commit()
    print('Mark OK!')


if __name__ == '__main__':
    app.run(debug=True)

