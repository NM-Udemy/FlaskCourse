from wtforms.form import Form
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from loginapp.models import User


class LoginForm(Form):
    email = StringField('メール: ', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード: ', validators=[DataRequired()])
    submit = SubmitField('ログイン')


class RegistForm(Form):
    email = StringField('メール: ', validators=[DataRequired(), Email()])
    username = StringField('名前: ', validators=[DataRequired()])
    password = PasswordField('パスワード: ', validators=[DataRequired()])
    password_confirm = PasswordField('パスワード再入力: ')
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_by_email(field.data):
            raise ValidationError('メールアドレスが登録されています')
