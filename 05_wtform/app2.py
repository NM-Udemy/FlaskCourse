from flask import (
    Flask, render_template, request, session, redirect, url_for, flash
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
from datetime import date

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

def validate_name2(form, field): # バリデーション自作
    if field.data == 'nanashi2':
        raise ValidationError('その名前も登録できません')

class UserForm(Form):
    name = StringField('名前: ', validators=[validate_name2, DataRequired('データを入力してください')], widget=TextArea(), default='Flask太郎')
    age = IntegerField('年齢: ', validators=[NumberRange(0, 100, '正しくない値です')])
    password = PasswordField(
        'パスワード: ', validators=[Length(1, 10, '長さは10文字以内です'), 
        EqualTo('confirm_password', 'パスワードが一致しません')]
    )
    confirm_password = PasswordField('パスワード再入力: ')
    birthday = DateField('誕生日: ', format='%Y/%m/%d', render_kw={"placeholder": "yyyy/mm/dd"})
    gender = RadioField(
        '性別: ', choices=[('man', '男性'), ('woman', '女性')], default='man'
    )
    major = SelectField('専攻: ', choices=[('bungaku', '文学部'),\
         ('hougaku', '法学部'), ('rigaku', '理学部')])
    is_japanese = BooleanField('日本人？:')
    message = TextAreaField('メッセージ: ')
    submit = SubmitField('送信')

    def validate_name(self, field):
        if field.data == 'nanashi':
            raise ValidationError('その名前は利用できません')
    
    def validate(self):
        if not super(UserForm, self).validate():
            return False
        today = date.today() # 今日の日付
        birthday = self.birthday.data
        birthday_of_this_age = birthday.replace(year=birthday.year + self.age.data)
        if 0 <= (today - birthday_of_this_age).days <= 365: # この場合正しい年齢
            return True
        flash("年齢と誕生日が正しくないです")
        return False


@app.route('/', methods=['GET','POST'])
def index():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        # sessionにデータを挿入する
        session['name'] = form.name.data
        session['age'] = form.age.data
        session['birthday'] = form.birthday.data
        session['gender'] = form.gender.data
        session['major'] = form.major.data
        session['nationality'] = '日本人' if \
            form.is_japanese.data else '外国人'
        session['message'] = form.message.data
        return redirect(url_for('show_user'))
    
    return render_template('user_regist.html', form=form)

@app.route('/show_user')
def show_user():
    return render_template('show_user.html')

if __name__ == '__main__':
    app.run(debug=True)
