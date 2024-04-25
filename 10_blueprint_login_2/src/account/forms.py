from flask_wtf import FlaskForm
from flask import flash
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from .models import User

class RegisterForm(FlaskForm):
    username = StringField('名前', validators=[
        DataRequired()
    ])
    email = StringField('メール', validators=[DataRequired(), 
                                           Email('メールアドレスを設定して')])
    password = PasswordField(
        'パスワード',
        validators=[DataRequired(), EqualTo('password_confirm', message="パスワードが一致しない")]
    )
    password_confirm = PasswordField('パスワード確認', validators=[DataRequired()])
    submit = SubmitField('登録')
    
    def validate_username(self, field):
        username = field.data
        if User.select_by_username(username):
            raise ValidationError("そのユーザーは存在します")
    
    def validate_email(self, field):
        email = field.data
        if User.select_by_email(email):
            raise ValidationError("そのメールアドレスは存在します")
    
    

class LoginForm(FlaskForm):
    email = StringField('メール', validators=[DataRequired(), 
                                           Email('メールアドレスを設定して')])
    password = PasswordField(
        'パスワード',
        validators=[DataRequired()]
    )
    submit = SubmitField('ログイン')

    def validate(self, extra_validators=None):
        if not super(LoginForm, self).validate():
            return False
        
        email = self.email.data
        password = self.password.data
        
        user = User.select_by_email(email)
        
        if not user:
            flash("認証が誤っています")
            return False
        
        if not user.validate_password(password):
            flash("認証が誤っています")
            return False
        
        return True
