from flask import Flask, render_template, redirect, url_for, abort
from datetime import datetime

app = Flask(__name__)


# born_yearテンプレートの自作。
@app.template_filter('born_year')
def calcurate_born_year(age):
    now_timestamp = datetime.now() # 現在のタイムスタンプ作成
    return str(now_timestamp.year - int(age))

# born_yearテンプレートの自作。
@app.template_filter('reverse_name')
def reverse(name):
    return name[-1::-1] # 文字列を逆順に表示

@app.route('/')
def index():
    return render_template('index.html') # templates/index.htmlを表示

@app.route('/home/<string:user_name>/<int:age>')
def home(user_name, age):
    # login_user = user_name
    login_user = {
        'name': user_name,
        'age': age
    }
    # templates/home.htmlにuser_infoという名前でlogin_user変数の値を渡す
    return render_template('home.html', user_info=login_user)

class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/userlist')
def user_list():
    # users = [
    #     'Taro', 'Jiro', 'Saburo', 'Shiro', 'Hanako'
    # ]
    users = [
        UserInfo('Taro',21), UserInfo('Jiro',32), UserInfo('Hanako',31)
    ]
    is_login = False
    # templates/userlist.htmlにusersという名前でusers変数の値,is_loginという名前でis_login変数の値を渡す
    return render_template('userlist.html', users=users, is_login=is_login)

@app.route('/user/<string:user_name>/<int:age>')
def user(user_name, age):
    if user_name in ['Taro', 'Jiro', 'Saburo']:
        # /homeにリダイレクトする
        return redirect(url_for('home', user_name=user_name, age=age))
    else:
        # 500エラーを発生させる
        abort(500, 'そのユーザはリダイレクトできません')

# 500エラーの場合の処理を定義
@app.errorhandler(500)
def system_error(error):
    error_description = error.description
    return render_template('system_error.html', error_description=error_description), 500

# 404(ページが見つからない)エラーの場合の処理を定義
@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
# templates/index.html