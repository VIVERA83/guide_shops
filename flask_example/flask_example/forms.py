from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, Field, HiddenField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from wtforms.widgets import html_params
from flask import Markup
import re


class HeaderWidget:
    html_params = staticmethod(html_params)

    def __init__(self, text=''):
        self.input_type = "h3"
        self.text = text

    def __call__(self, field, **kwargs):
        return Markup('<h3 %s>%s</h3>' % (self.html_params(**kwargs), field.text))


class HeaderField(Field):
    widget = HeaderWidget()

    def __init__(self, label=None, validators=None, text='Заголовок', **kwargs):
        super(HeaderField, self).__init__(label, validators, **kwargs)
        self.text = text

    def _value(self):
        if self.data:
            return u''.join(self.data)
        else:
            return u''


class MessageWidget:
    html_params = staticmethod(html_params)

    def __init__(self, text=''):
        self.input_type = "span"
        self.text = text

    def __call__(self, field, **kwargs):
        return Markup('<h5 %s>%s</h5>' % (self.html_params(**kwargs), field.text))


class MessageField(Field):
    widget = HeaderWidget()

    def __init__(self, label=None, validators=None, text='Напиши здесь', **kwargs):
        super(MessageField, self).__init__(label, validators, **kwargs)
        self.text = text

    def _value(self):
        if self.data:
            return u''.join(self.data)
        else:
            return u''


class TelValidator(object):

    def __init__(self, message=None):
        if message is None:
            message = "Ошибка, пример +7981-880-41-44"
        self.message = message

    def __call__(self, form, field):
        pattern = "^((8|\+7)[\- ]?)?(\(?\d{3,4}\)?[\- ]?)?[\d\- ]{5,10}$"

        if not field.data:
            raise ValidationError('Поле не может быть пустым')

        if not re.fullmatch(pattern, field.data):
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    id_form = "registration_form"
    name_form = HiddenField(render_kw={'value': id_form})
    header = HeaderField(text='Регистрация')
    name = StringField(validators=[DataRequired(),
                                   Length(min=4, max=20,
                                          message="Длинна имени от 4 до 20 символов")],
                       render_kw={"placeholder": "Имя"})
    phone = StringField(validators=[TelValidator()], render_kw={"placeholder": "тел. в формате +7(777)777-777-77"})
    psw = PasswordField(validators=[DataRequired(),
                                    Length(min=6, max=20,
                                           message="Длинна пароля от 6 до 20 символов")],
                        render_kw={"placeholder": "Пароль"})
    psw2 = PasswordField(validators=[EqualTo("psw", message="Пароли не совпадают")],
                         render_kw={"placeholder": "Повторите пароль"})
    submit = SubmitField("Зарегистрироваться", render_kw={"class": "button"})
    text = MessageField(text='Нажимая на "Зарегистрироваться" вы потверждаете что прочитали и согласны с нашими '
                             'условиями и политикой конфидициальности')


class LoginForm(FlaskForm):
    id_form = "login_form"
    name_form = HiddenField(render_kw={'value': id_form})
    header = HeaderField(text='Авторизация')
    phone = StringField("phone",
                        validators=[TelValidator()],
                        render_kw={"placeholder": "Телефон, пример: 9818618643"})
    psw = PasswordField("Пароль :",
                        validators=[DataRequired(message="Пароль не может быть из пробелов"),
                                    Length(min=6, max=10, message="Ошибка ввода пароля")],
                        render_kw={"placeholder": "Пароль"})
    submit = SubmitField("Войти")


class SearchForm(FlaskForm):
    id_form = "search_form"
    test = StringField(validators=[TelValidator()], render_kw={"placeholder": "тел. в формате +7(981)861-44-44"})
    name_form = HiddenField(render_kw={'value': id_form})
    header = HeaderField(text='Поиск магазина')
    shop = StringField("name", validators=[DataRequired(), Length(min=4, max=20)],
                       render_kw={"placeholder": "Магазин, например: Манса"})
    submit = SubmitField("Найти")
