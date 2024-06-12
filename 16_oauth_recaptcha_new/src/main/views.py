from flask import render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from . import main_bp
from .models import Memo
from .forms import MemoForm, DeleteMemoForm

@main_bp.route('/')
def home():
    return render_template('main/home.html')

@main_bp.route('/memos', methods=['GET', 'POST'])
@login_required
def memos():
    form = MemoForm(request.form)
    if request.method=="POST" and form.validate_on_submit():
        Memo.add_memo(
            form.title.data,
            form.content.data,
            current_user
        )
        return redirect(url_for('main.memos'))
    memo_list = Memo.get_user_memos(current_user)
    delete_form = DeleteMemoForm()
    return render_template('main/memos.html',
                           memo_list=memo_list,
                           form=form,
                           delete_form=delete_form,
                           )
    
@main_bp.route('/memos/delete', methods=['POST'])
@login_required
def delete_memo():
    form = DeleteMemoForm(request.form)
    if form.validate_on_submit():
        Memo.delete_memo(form.id.data)
    return redirect(url_for('main.memos'))

@main_bp.route('/memos/update', methods=['POST'])
@login_required
def update_memo():
    form = MemoForm(request.form)
    if form.validate_on_submit():
        memo_id = form.id.data
        title = form.title.data
        content = form.content.data
        Memo.update_memo(memo_id, title, content)
    return redirect(url_for('main.memos'))

@main_bp.route("/get_data")
def get_data():
    data = {
        "title": "サンプルデータ",
        "content": "これはサンプルデータです"
    }
    return jsonify(data)

@main_bp.route("/create_memo", methods=["POST"])
def create_memo():
    form = MemoForm(request.form)
    if form.validate_on_submit():
        memo = Memo.add_memo(
            form.title.data,
            form.content.data,
            current_user
        )
        return jsonify({
            "status": "success",
            "id": memo.id,
            "title": memo.title,
            "content": memo.content,
        })
    return jsonify({"status": "fail"})