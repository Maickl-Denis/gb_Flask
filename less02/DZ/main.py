from flask import Flask, request, render_template, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = b"6acbc1439c6afcbf8906074d2bb33033afed8530e014811e7d760c66f87ff47d"

@app.route('/')
def index():
    return ("Hi!<br>"
            "1. <a href='/DZ'>DZ</a>")


@app.get('/DZ/')
def DZ():
    context = {'title': 'Форма'}
    return render_template('DZ.html', **context)

@app.post('/DZ/')
def DZ_cooki():
    session['name'] = request.form.get('name')
    session['e_mail'] = request.form.get('email')
    return redirect(url_for('result'))

@app.route('/result/', methods=['GET', 'POST'])
def result():
    if 'name' in session:
        context = {'name': session.get('name'), 'email': session.get('e_mail'), 'title': 'Авторизация успеша'}
        return render_template('result.html', **context)
    else:
        return redirect(url_for('DZ'))

@app.post('/logout/')
def logout():
    session.pop('name', None)
    session.pop('e_mail', None)
    return redirect(url_for('DZ'))

if __name__ == '__main__':
    app.run(debug=True)