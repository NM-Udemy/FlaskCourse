from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, FileField, PasswordField,
    SubmitField, HiddenField, TextAreaField
)
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_login import current_user
from flask import flash

from flaskr.models import User, UserConnect

# ログイン用のForm
class LoginForm(FlaskForm):
    email = StringField(
        'メール: ', validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'パスワード: ',
        validators=[DataRequired(),
        EqualTo('confirm_password', message='パスワードが一致しません')]
    )
    confirm_password = PasswordField(
        'パスワード再入力: ', validators=[DataRequired()]
    )
    submit = SubmitField('ログイン')

# 登録用のForm
class RegisterForm(FlaskForm):
    email = StringField(
        'メール: ', validators=[DataRequired(), Email('メールアドレスが誤っています')]
    )
    username = StringField('名前: ', validators=[DataRequired()])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_user_by_email(field.data):
            raise ValidationError('メールアドレスはすでに登録されています')

# パスワード設定用のフォーム
class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        'パスワード',
        validators=[DataRequired(), EqualTo('confirm_password', message='パスワードが一致しません')]
    )
    confirm_password = PasswordField(
        'パスワード確認: ', validators=[DataRequired()]
    )
    submit = SubmitField('パスワードを更新する')
    def validate_password(self, field):
        if len(field.data) < 8:
            raise ValidationError('パスワードは8文字以上です')


class ForgotPasswordForm(FlaskForm):
    email = StringField('メール: ', validators=[DataRequired(), Email()])
    submit = SubmitField('パスワードを再設定する')

    def validate_email(self, field):
        if not User.select_user_by_email(field.data):
            raise ValidationError('そのメールアドレスは存在しません')



class UserForm(FlaskForm):
    email = StringField(
        'メール: ', validators=[DataRequired(), Email('メールアドレスが誤っています')]
    )
    username = StringField('名前: ', validators=[DataRequired()])
    picture_path = FileField('ファイルアップロード')
    submit = SubmitField('登録情報更新')

    def validate(self):
        if not super(FlaskForm, self).validate():
            return False
        user = User.select_user_by_email(self.email.data)
        if user:
            if user.id != int(current_user.get_id()):
                flash('そのメールアドレスはすでに登録されています')
                return False
        return True

class ChangePasswordForm(FlaskForm):
    password = PasswordField(
        'パスワード',
        validators=[DataRequired(), EqualTo('confirm_password', message='パスワードが一致しません')]
    )
    confirm_password = PasswordField(
        'パスワード確認: ', validators=[DataRequired()]
    )
    submit = SubmitField('パスワードの更新')
    def validate_password(self, field):
        if len(field.data) < 8:
            raise ValidationError('パスワードは8文字以上です')

class UserSearchForm(FlaskForm):
    username = StringField(
        '名前: ', validators=[DataRequired()]
    )
    submit = SubmitField('ユーザ検索')

class ConnectForm(FlaskForm):
    connect_condition = HiddenField()
    to_user_id = HiddenField()
    submit = SubmitField()

class MessageForm(FlaskForm):
    to_user_id = HiddenField()
    message = TextAreaField()
    submit = SubmitField('メッセージ送信')

    def validate(self):
        if not super(FlaskForm, self).validate():
            return False
        is_friend = UserConnect.is_friend(self.to_user_id.data)
        if not is_friend:
            return False
        return True