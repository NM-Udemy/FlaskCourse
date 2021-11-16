from flask import Blueprint, request, render_template, redirect, url_for, current_app
from flask_login import login_user, login_required, logout_user, current_user
from flaskr.forms import LoginForm, RegisterForm
from flaskr.models import User
from flask import g
import logging
import time

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    current_app.logger.info('Home画面です')
    return render_template('home.html')

# ログインしていないと実行されない(login_userが実行されていないと)
# ログインしていない場合はlogin関数に飛ばされる
@bp.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user() # ログアウトできる
    return redirect(url_for('app.home'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.select_by_email(form.email.data)
        # emailから取得したUserのパスワードとクライアントが入力したパスワードが一致するか
        if user and user.validate_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next') # 次のURL
            if not next:
                next = url_for('app.welcome')
            return redirect(next)
    return render_template('login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data
        )
        user.add_user()
        return redirect(url_for('app.login'))
    return render_template('register.html', form=form)

@bp.route('/user')
@login_required
def user():
    return render_template('user.html')

@bp.before_request
def before_request():
    g.start_time =  time.time()
    user_name = ''
    if current_user.is_authenticated:
        user_name = current_user.username
    current_app.logger.info(
        f'user: {user_name}, {request.remote_addr}, {request.method}, {request.url}, {request.data}'
    )

@bp.after_request
def after_request(response):
    user_name = ''
    if current_user.is_authenticated:
        user_name = current_user.username
    current_app.logger.info(
        f'user: {user_name}, {request.remote_addr}, {request.method}, {request.url}, {request.data}, {response.status}'
    )
    end_time = time.time()
    logging.getLogger('performance').info(
        f'{request.method}, {request.url}, execution time = {end_time - g.start_time}'
    )
    return response