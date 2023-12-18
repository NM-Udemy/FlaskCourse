from flask import Flask, render_template, redirect, url_for, abort
from custom_filters import reverse, calculate_birth_year


# app = Flask(__name__, static_folder="custom_static")
app = Flask(__name__)
app.add_template_filter(reverse, 'reverse_name')
app.add_template_filter(calculate_birth_year, 'birth_year')

# @app.template_filter('reverse_name')
# def reverse(name):
#     return name[::-1]

# @app.template_filter('birth_year')
# def calculate_birth_year(age):
#     current_year = datetime.datetime.now().year
#     birth_year = current_year - age
#     return birth_year

@app.route('/')
def index():
    return render_template('index.html', user="John".upper())

class UserInfo:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self, message=""):
        return f"{self.name}です。よろしくお願い申し上げます。{message}"

@app.route('/home/<string:user_name>/<int:age>')
def home(user_name, age):
    # login_user = user_name
    # user_info = {
    #     'name': user_name,
    #     'age': age
    # }
    user_info = UserInfo(user_name, age)
    return render_template('home.html', user_info=user_info)

@app.route('/userlist')
def user_list():
    users = [
        'Taro', 'Jiro', 'Saburo', 'Shiro'
    ]
    is_login = False
    return render_template('userlist.html', users=users, is_login=is_login)

@app.route('/user/<user_name>/<int:age>')
def user(user_name, age):
    if user_name in ['Taro', 'Jiro', 'Saburo']:
        return redirect(url_for('home', user_name=user_name, age=age))
    elif user_name == 'Shiro':
        return redirect('https://google.com')
    else:
        abort(500, 'そのユーザーはリダイレクトできません')

@app.errorhandler(500)
def system_error(error):
    error_description = error.description
    return render_template('system_error.html', 
                           error_description=error_description), 500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
