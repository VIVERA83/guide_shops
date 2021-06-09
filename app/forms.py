from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, Field
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange, EqualTo
from wtforms.widgets import html_params
from flask import Markup


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
        return Markup('<span %s>%s</span>' % (self.html_params(**kwargs), field.text))


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


class RegistrationForm(FlaskForm):
    id_form = "registration"
    header = HeaderField(text='Заголовок')
    name = StringField(validators=[InputRequired("ПРивет"), DataRequired(), Length(min=4, max=20)],
                       render_kw={"placeholder": "Имя"})
    phone = IntegerField(validators=[DataRequired(), NumberRange(min=9000000, max=9999999)],
                         render_kw={"placeholder": "Телефон, пример: 9818618643"})
    psw = PasswordField(validators=[DataRequired(), Length(min=4, max=100)],
                        render_kw={"placeholder": "Пароль"})
    psw = PasswordField(validators=[InputRequired(), DataRequired(), EqualTo(psw)],
                        render_kw={"placeholder": "Повторите пароль"})
    submit = SubmitField("Зарегистрироваться", render_kw={"class": "button"})
    text = MessageField(text='Нажимая на "Зарегистрироваться" вы потверждаете что прочитали и согласны с нашими условиями'
                        ' и политекой конфидициальности')


class LoginForm(FlaskForm):
    id_form = "login_form"
    phone = IntegerField("phone", validators=[NumberRange(min=9000000, max=9999999)],
                         render_kw={"placeholder": "Телефон, пример: 9818618643"})
    psw = PasswordField("Пароль :", validators=[DataRequired(), Length(min=4, max=100)],
                        render_kw={"placeholder": "Пароль"})

    # remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")


class SearchForm(FlaskForm):
    id_form = "search_form"
    shop = StringField("name", validators=[DataRequired(), Length(min=4, max=20)],
                       render_kw={"placeholder": "Магазин, например: Манса"})
    submit = SubmitField("Найти")

# Не трогать
# class InlineButtonWidget(object):
#     html_params = staticmethod(html_params)
#
#     def __init__(self, input_type='submit', text=''):
#         self.input_type = input_type
#         self.text = text
#
#     def __call__(self, field, **kwargs):
#         kwargs.setdefault('id', field.id)
#         kwargs.setdefault('type', self.input_type)
#         if 'value' not in kwargs:
#             kwargs['value'] = field._value()
#         return Markup('<button type="submit" %s><span>%s</span></button>' % (self.html_params(name=field.name, **kwargs), field.text))
#
# # Не трогать
# class InlineButton(Field):
#   widget = InlineButtonWidget()
#
#   def __init__(self, label=None, validators=None, text='Save', **kwargs):
#     super(InlineButton, self).__init__(label, validators, **kwargs)
#     self.text = text
#
#   def _value(self):
#         if self.data:
#             return u''.join(self.data)
#         else:
#             return u''
# class SignupForm(Form):
#    # name = TextField('Name', [Length(min=1, max=200)])
#    submit = InlineButton('submit', text='Save', description='Save this')
