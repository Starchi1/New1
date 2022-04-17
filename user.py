from flask_wtf import FlaskForm
from wtforms import StringField
import sqlalchemy
from wtforms.validators import DataRequired
from wtforms import PasswordField, SubmitField

class RegisterForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')