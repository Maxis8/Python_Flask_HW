# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/num/', methods=['POST', 'GET'])
def input_number():
    form = """
    <form method="post" enctype="multipart/form-data">
    <input type="text" placeholder="Enter number" name="text"><br>
    <input type="submit" value="Enter">
</form>
    """
    if request.method == 'POST':
        num_input = request.form.get('text')
        num_input = int(num_input)
        res = num_input * num_input
        return redirect(url_for('result_age', res_num=num_input, sq_num=res))

    return form


@app.route('/result/<res_num>-<sq_num>')
def result_age(sq_num, res_num):
    return f' Num: {res_num} Sqrt:{sq_num}  '


if __name__ == '__main__':
    app.run(debug=True)