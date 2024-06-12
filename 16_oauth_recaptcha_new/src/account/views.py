from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from . import account_bp
from .forms import RegisterForm, LoginForm, ChangePasswordForm
from .models import User
from datetime import timedelta
from flask_dance.contrib.google import google
import string
import random

@account_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        User.add_user(form.username.data, form.email.data, form.password.data)
        return redirect(url_for('main.home'))
    return render_template('account/register.html', form=form)


@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print(form.recaptcha())
    data = request.form
    
    for key, value in data.items():
        print(f'{key}: {value}')
    
    if request.method == "POST" and form.validate_on_submit():
        user = User.select_by_email(form.email.data)
        login_user(user, remember=True)
        print('ログイン完了')
        
        # nextパラメータを取得
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        
        return redirect(url_for('account.user'))
    return render_template('account/login.html', form=form)

@account_bp.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login")) # Googleログインにリダイレクト
    response = google.get("/oauth2/v2/userinfo") # 認証情報の取得
    username = response.json()['name']
    email = response.json()['email']
    # 英語大文字小文字のランダム16文字
    random_password = ''.join(random.choices(string.ascii_letters, k=16))
    user = User.select_by_email(email)
    if not user: # User作成
        user = User.add_user(
            username=username,
            email=email,
            password=random_password,
        )
    login_user(user, remember=True)
    return redirect(url_for('account.change_password'))


@account_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    if google.authorized:
        token = google.token["access_token"]
        response = google.post(
            "https://accounts.google.com/o/oauth2/revoke",
            params={"token": token},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        if response.ok:
            del google.token
    logout_user()
    return redirect(url_for('main.home'))

@account_bp.route('/')
@login_required
def user():
    print(current_user.is_authenticated)
    return render_template('account/user.html')

@account_bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        if current_user.change_password(form.new_password.data):
            return redirect(url_for('account.user'))
    return render_template('account/change_password.html', form=form)
