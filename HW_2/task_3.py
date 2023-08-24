# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".


from flask import Flask, flash, redirect, render_template, request, url_for
import secrets
secrets.token_hex()

app = Flask(__name__)
app.secret_key = secrets.token_hex()





@app.route('/form/', methods=['GET', 'POST'])
def form():

    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash.html')


if __name__ == '__main__':
    app.run(debug=True)