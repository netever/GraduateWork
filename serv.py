from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_required
import save_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_user', methods=['POST'])
def new_user():
    role = request.form['role']
    email = request.form['email']
    save_data.save_user(email, role)
    return render_template('new_user.html')


@app.route('/del_user', methods=['POST'])
def del_user():
    email = request.form['email']
    save_data.del_user(email)
    return render_template('del_user.html')


@app.route('/admin/')
@login_required
def admin():
    return render_template('admin.html')


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('login')
        password = request.form.get('password')

        if save_data.checkuser(username, password):
            message = "Correct username and password"
            return render_template('admin.html', message=message)
        else:
            message = "Wrong username or password"

    return render_template('index.html', message=message)


@app.route('/parametres', methods=['post', 'get'])
def parametres():
    send_vk = request.form['send_vk']
    send_tel = request.form['send_tel']
    send_mail = request.form['send_mail']
    save_data.changeparam(send_vk, send_tel, send_mail)
    return render_template('parametres.html')


if __name__ == "__main__":
    app.run()
