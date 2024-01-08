from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form

app = Flask(__name__)

app.config['SECRET_KEY'] = b'Tly\x1fs\xef\x12q\x0e\x9a\xda\xe6\xb8EC\x0f'


class UserForm(Form):
    name = StringField('名前')
    age = IntegerField('年齢')
    submit = SubmitField('Submit')

@app.route('/', methods=["GET", "POST"])
def index():
    name = age = ''
    form = UserForm(request.form) # name, ageに値を設定
    if request.method == "POST":
        if form.validate(): # name, ageの値が正しいかチェック
            name = form.name.data
            age = form.age.data
            form = UserForm() # Formの初期化
        else:
            print('入力内容に誤りがあります')
    return render_template('index.html', form=form, name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)