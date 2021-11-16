from flask import Blueprint, flash, request, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from loginapp.models import User
from flask_dance.contrib.google import google
from loginapp import google_blueprint
from loginapp.forms import LoginForm, RegistForm
import flask_session_captcha


bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login")) # Googleのログイン画面にリダイレクト
    resp = google.get("/oauth2/v2/userinfo") # 認証情報を取得
    assert resp.ok, resp.text
    email = resp.json()['email']
    user = User.select_by_email(email)
    if not user:
        user = User(email=email)
        user.add_user()
    login_user(user, remember=True)
    return render_template(
        'welcome.html', email=email
    )

@bp.route('/user')
@login_required
def user():
    return render_template('user.html')

@bp.route('/logout')
@login_required
def logout():
    if google.authorized:
        token = google_blueprint.token['access_token']
        resp = google.post(
            "https://accounts.google.com/o/oauth2/revoke",
            params={"token": token},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        assert resp.ok,resp.text
        del google_blueprint.token # token削除
    logout_user()
    return redirect(url_for('app.home'))

@bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method=='POST' and form.validate():
        user = User.select_by_email(form.email.data)
        if user and user.validate_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next:
                next = url_for('app.home')
            return redirect(next)
    return render_template('login.html', form=form)


@bp.route('/regist', methods=['GET', 'POST'])
def regist():
    form = RegistForm(request.form)
    if request.method == 'POST' and form.validate():
        if flask_session_captcha.session.get('captcha_answer') != request.form.get('captcha'):
            flash('入力した値が画像の者と違います')
            return render_template('regist.html', form=form)
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        user.add_user()
        return redirect(url_for('app.home'))
    return render_template('regist.html', form=form)