import re
from os import path
from flask import Flask, render_template, request, flash
from flask_login import LoginManager, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, Users
from .forms import RegistrationForm, LoginForm, SearchForm
from .logins import UserLogin

app = Flask(__name__)
app.config.from_pyfile(path.join(app.root_path, "config.py"))
login_manager = LoginManager(app)

db.init_app(app)
app.app_context().push()
db.create_all()


def converting_to_integer(message: str) -> int:
    return int(''.join(re.findall("\\d", message)))


def registration(phone_int):
    hash_psw = generate_password_hash(request.form['psw'])
    user = Users(name=request.form['name'],
                 phone=phone_int,
                 psw=hash_psw)
    db.session.add(user)
    db.session.commit()


@login_manager.user_loader
@app.route("/", methods=["GET", "POST"])
def index():
    forms = {"registration_form": RegistrationForm(),
             "login_form": LoginForm(),
             "search_form": SearchForm()}
    visible = None

    if request.method == "POST":
        active_form = request.form['name_form']
        if forms[active_form].validate_on_submit():
            if active_form == "registration_form":
                phone_int = converting_to_integer(request.form['phone'])  #
                res = Users.query.filter_by(phone=phone_int).first()  #
                if not res:
                    registration(phone_int)
                    return "Успешно зарегистрировались"  # создай форму успешной регистрации, переход в профиль
                else:
                    flash("Ошибка регистрации, такой телефон уже зарегистрирован", category="error")
                    visible = forms[active_form].id_form
                    # Выделить красным ошибки
                    return render_template("index.html", visible=visible,
                                           forms=forms)  # "Ошибка - ТАкой номер телефона уже зарегистрировались"
            elif active_form == "login_form":
                phone_int = converting_to_integer(request.form['phone'])  #
                user = Users.query.filter_by(phone=phone_int).first()
                if user and check_password_hash(user.psw, request.form['psw']):
                    login_user(UserLogin(user.id))
                    return "Вошли"
                else:
                    flash("Ошибка Авторизации, телефон либо пароль указаны не верно", category="error")
                    visible = forms[active_form].id_form
                    # Выделить красным ошибки
                    # "Ошибка - ТАкой номер телефона уже зарегистрировались"
                    return render_template("index.html", visible=visible, forms=forms)
            elif active_form == "search_form":
                return "Нашли или нет"
        else:
            visible = forms[active_form].id_form
    return render_template("index.html", visible=visible, forms=forms)


def run_me(host: str = app.config["HOST"], port: int = app.config["PORT"]):
    app.run(host=host, port=port)


if __name__ == '__main__':
    run_me()
