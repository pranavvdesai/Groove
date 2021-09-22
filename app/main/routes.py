from flask import Blueprint, render_template, request, redirect, session
from app import cursor
from app import conn
from app.users.auth_routes import email, password

main = Blueprint('main', __name__)

# Main Routes


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


@main.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')


@main.route('/form')
def form():
    return render_template('form.html')

# Questionnaire


@main.route('/home', methods=['POST'])
def form_data():
    global result
    if request.method == "POST":
        req = request.form
        movie = req['movie']
        music = req['music']
        sport = req['sport']
        choice = req['choice']
        result = movie+music+sport+choice
        cursor.execute(
            """SELECT * FROM `users`  WHERE `email` LIKE '{}' AND `password` LIKE '{}' """.format(email, password))
        user = cursor.fetchone()
        cursor.execute(
            """UPDATE `users` set results='{}' WHERE email='{}' """.format(result, email))
        conn.commit()
        conn.commit()
        return render_template('home.html')
