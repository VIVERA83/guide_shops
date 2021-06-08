from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(min=4, max=20)])
    phone = IntegerField("phone", validators=[NumberRange(min=9000000, max=9999999)])
    psw = PasswordField("Пароль :", validators=[DataRequired(), Length(min=4, max=100)])
    psw = PasswordField("Пароль :", validators=[InputRequired(), DataRequired(), EqualTo(psw)])
    submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    phone = IntegerField("phone", validators=[NumberRange(min=9000000, max=9999999)])
    psw = PasswordField("Пароль :", validators=[DataRequired(), Length(min=4, max=100)])
    # remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")


class SearchForm(FlaskForm):
    shop = StringField("name", validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("Найти")
