from flask import Flask, render_template, url_for, request, get_flashed_messages, flash
from os import path
from models import db
from forms import RegistrationForm, LoginForm, SearchForm
from werkzeug.security import generate_password_hash
from models import Users
import re

app = Flask(__name__)
app.config.from_pyfile(path.join(app.root_path, "config.py"))
db.init_app(app)
app.app_context().push()
db.create_all()


def converting_to_integer(message: str) -> int:
    return int(''.join(re.findall("\d", message)))


@app.route("/", methods=["GET", "POST"])
def index():
    forms = {"registration_form": RegistrationForm(),
             "login_form": LoginForm(),
             "search_form": SearchForm()}
    visible = None

    if request.method == "POST":
        active_form = request.form['name_form']
        print(f"request_form_name = {active_form}")
        if forms[active_form].validate_on_submit():
            if active_form == "registration_form":
                phone_int = converting_to_integer(request.form['phone'])
                res = Users.query.filter_by(phone=phone_int).first()
                print(f"request_form_name = {res}")
                if not res:
                    hash_psw = generate_password_hash(request.form['psw'])
                    user = Users(name=request.form['name'],
                                 phone=converting_to_integer(request.form['phone']),
                                 psw=hash_psw)
                    db.session.add(user)
                    db.session.commit()
                    print("Успешно зарегистрировались")
                    return "Успешно зарегистрировались"  # создай форму успешной регистрации, переход в профиль
                else:
                    flash("Ошибка регистрации, такой телефон уже зарегистрирован", category="error")
                    visible = forms[active_form].id_form
                    # Выделить красным ошибки
                    return render_template("index.html", visible=visible, forms=forms)# "Ошибка - ТАкой номер телефона уже зарегистрировались"
            elif active_form == "login_form":
                print("Войти")
                return "Вошли"
            elif active_form == "search_form":
                print("Найти")
                return "Нашли или нет"
        else:
            visible = forms[active_form].id_form
            print(f"visible={visible}")

    return render_template("index.html", visible=visible, forms=forms)


if __name__ == '__main__':
    # [print(key, value) for key, value in app.config.items()]

    app.run(host=app.config["HOST"], port=app.config["PORT"])
