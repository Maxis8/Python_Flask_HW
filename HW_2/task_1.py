# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/age/', methods=['POST', 'GET'])
def input_age():
    form = """
    <form method="post" enctype="multipart/form-data">
    <input type="text" placeholder="Enter age" name="text"><br>
    <input type="submit" value="Enter">
</form>
    """
    if request.method == 'POST':
        age_input = request.form.get('text')
        age_input = int(age_input)
        if 0 < age_input < 130:
            return redirect(url_for('result_age', res_text=age_input))
        else:
            return redirect(url_for('get_error', res_text=age_input))
    return form


@app.route('/result/<res_text>')
def result_age(res_text):
    return f'{res_text} '


@app.route('/error/<res_text>')
def get_error(res_text):
    return f'Age {res_text} is not correct'


if __name__ == '__main__':
    app.run(debug=True)