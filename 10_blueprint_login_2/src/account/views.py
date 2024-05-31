from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from . import account_bp
from .forms import RegisterForm, LoginForm
from .models import User
from datetime import timedelta

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

@account_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@account_bp.route('/')
@login_required
def user():
    print(current_user.is_authenticated)
    return render_template('account/user.html')

