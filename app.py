from flask import Flask, render_template, request, redirect, url_for
from db import init_db, check_credentials

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Проверяем учетные данные
        if check_credentials(username, password):
            return redirect(url_for('success'))
        else:
            return redirect(url_for('error'))
    else:
        return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)