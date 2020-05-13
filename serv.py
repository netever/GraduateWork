from flask import Flask, render_template, redirect, url_for, request
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


if __name__ == "__main__":
    app.run()