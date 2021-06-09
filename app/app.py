from flask import Flask, render_template, url_for, request, get_flashed_messages, flash
from os import path
from models import db
from forms import RegistrationForm, LoginForm, SearchForm

app = Flask(__name__)
app.config.from_pyfile(path.join(app.root_path, "config.py"))
db.init_app(app)
app.app_context().push()
db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    visible = None
    if request.method == "POST":
        print("Нажата кнопка: ", request.form.keys())
    forms = [RegistrationForm(), LoginForm(), SearchForm()]
        # {"registration": RegistrationForm(), "login_form": LoginForm(), "search_form": SearchForm()}
    # forms_id = ["registration","login_form", "search_form"]
    # registration_form = RegistrationForm()
    # id_form = "registration"
    # print(registration_form.__dict__)
    # login_form = LoginForm()
    # print(forms["registration"].id)
    if request.method == "POST":
        if request.form.get("login"):
            if len(request.form["phone"]) < 7:
                print("login")
                flash("Ошибка телефона", category="error")
                visible = 'block'

    return render_template("index.html", visible=visible, forms=forms)


if __name__ == '__main__':
    # [print(key, value) for key, value in app.config.items()]

    app.run(host=app.config["HOST"], port=app.config["PORT"])
