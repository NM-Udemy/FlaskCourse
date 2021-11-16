from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form


app = Flask(__name__)

# csrf_tokenを生成するためのSECRET_KEY
app.config['SECRET_KEY'] = b'TU\xa6\xfc\xec\xc8a\x7f\x9d\xad\x06\x7f\xb1\xe9qP'

class UserForm(Form): # name,age,submitを持つFormを作成
    name = StringField('名前')
    age = IntegerField('年齢')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = age = ''
    form = UserForm(request.form) # Requestをフォーム形式で取得
    if request.method == 'POST':
        if form.validate(): # フォームが適切か検証する
            name = form.name.data
            age = form.age.data
            form.name.data = ''
            form.age.data = ''
        else:
            print('入力内容に問題があります')

    return render_template('index.html', form=form, name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)