from flask import Flask, render_template, url_for, request, get_flashed_messages
from os import path
from models import db
from forms import RegistrationForm, LoginForm, SearchForm
from werkzeug.security import generate_password_hash
from models import Users

app = Flask(__name__)
app.config.from_pyfile(path.join(app.root_path, "config.py"))
db.init_app(app)
app.app_context().push()
db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    forms = {"Зарегистрироваться": RegistrationForm(),
             "Войти": LoginForm(),
             "Найти": SearchForm()}
    visible = None
    if request.method == "POST":
        if forms[request.form["submit"]].validate_on_submit():
            if request.form["submit"] == "Зарегистрироваться":
                hash_psw = generate_password_hash(request.form['psw'])
                user = Users(name=request.form['name'],
                             phone=request.form['phone'],
                             psw=hash_psw)
                db.session.add(user)
                db.session.commit()
            elif request.form["submit"] == "Войти":
                print("Войти")
            elif request.form["submit"] == "Найти":
                print("Найти")
        else:
            visible = forms[request.form["submit"]].id_form
            print(visible)

    return render_template("index.html", visible=visible, forms=forms)


# @app.route('/login', methods)
# def login():
#     print("LOGIN")
#     return "Привет"

if __name__ == '__main__':
    # [print(key, value) for key, value in app.config.items()]

    app.run(host=app.config["HOST"], port=app.config["PORT"])
