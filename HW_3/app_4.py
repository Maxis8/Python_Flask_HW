# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite) и выводиться сообщение
# об успешной регистрации. Если какое-то из обязательных полей не заполнено или данные не прошли валидацию,
# то должно выводиться соответствующее сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.


from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import CSRFProtect
import secrets

from HW_3.forms_04 import RegistrationForm
from HW_3.models_04 import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///regis.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'Hello'


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protection'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(username=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(email, password)
        return redirect(url_for('success', name=name))
        ...
    return render_template('register.html', form=form)


@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok ')


if __name__ == '__main__':
    app.run(debug=True)



