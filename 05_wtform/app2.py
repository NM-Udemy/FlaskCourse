# いろんなFormの処理
from flask import(
    Flask, render_template, request, session, redirect, url_for
)
from wtforms import Form
from wtforms import (
    StringField, IntegerField, BooleanField, DateField, PasswordField,
    RadioField, SelectField, TextAreaField, SubmitField
)
from wtforms.widgets import TextArea
from wtforms.validators import (
    DataRequired, EqualTo, Length, NumberRange, ValidationError
)
from wtforms.csrf.session import SessionCSRF
from datetime import date, timedelta


app = Flask(__name__)

app.config['SECRET_KEY'] = "mykey"

def check_name(form, field):
    if field.data == 'いいいい':
        raise ValidationError('その名前は使えません')


class UserForm(Form):
    name = StringField('名前: ', default="Flask太郎",
                       validators=[check_name, DataRequired(), Length(2, 20)],
                       render_kw={"size": 50},
                       widget=TextArea())
    age = IntegerField('年齢: ', validators=[NumberRange(0, 100)])
    password = PasswordField('パスワード: ')
    birthday = DateField('誕生日: ')
    gender = RadioField('性別: ', choices=[('man', '男性'), ('woman', '女性')],
                        default='man')
    major = SelectField('専攻: ', choices=[
        ('bungaku', '文学部'), ('hougaku', '法学部'), ('rigaku', '理学部')
    ])
    is_japanese = BooleanField('日本人か?: ', render_kw={'checked': True})
    message = TextAreaField('メッセージ: ', render_kw={'placeholder': "一言"})
    submit = SubmitField('送信')
    
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = b'aaaaaaabbbb'
        csrf_time_limit = timedelta(minutes=1)

        @property
        def csrf_context(self):
            return session
    
    def validate_name(self, field):
        if field.data == 'ああああ':
            raise ValidationError('その名前は利用できません')

    def validate(self):
        if not super(UserForm, self).validate():
            if self.csrf_token.errors:
                for i, error in enumerate(self.csrf_token.errors):
                    if error == 'CSRF token expired.':
                        self.csrf_token.errors[i] = 'セッションが切れています'
            return False
        today = date.today()
        calculated_age = today.year - self.birthday.data.year
        if calculated_age == self.age.data:
            return True
        self.age.errors.append('誕生日と一致しません')
        self.birthday.errors.append('年齢と一致しません')
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        session['name'] = form.name.data
        session['age'] = form.age.data
        session['birthday'] = form.birthday.data
        session['gender'] = form.gender.data
        session['major'] = form.major.data
        session['nationality'] = '日本人' if \
            form.is_japanese.data else '外国人'
        session['message'] = form.message.data
        return redirect(url_for('show_user'))
    print(form.name.errors)
    return render_template('user_regist.html', form=form)

@app.route('/show_user', methods=['POST', 'GET'])
def show_user():
    # form = UserForm(request.form)
    # if request.method == "POST" and form.validate():
    #     data['name'] = form.name.data
    #     data['age'] = form.age.data
    return render_template('show_user.html')

if __name__ == '__main__':
    app.run(debug=True)
