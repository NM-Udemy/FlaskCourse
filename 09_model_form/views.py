from forms import CreateForm, UpdateForm, DeleteForm
from flask import request, render_template, url_for, redirect
from models import db, Member
from app import app


@app.route('/')
@app.route('/member_list')
def member_list():
    # メンバー一覧表示
    members = Member.query.all()
    form = DeleteForm(request.form)
    return render_template('member_list.html', members=members, form=form)

@app.route('/create_member', methods=['GET', 'POST'])
def create_member():
# メンバー新規作成
    form = CreateForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        age = form.age.data
        comment = form.comment.data
        # トランザクション
        with db.session.begin(subtransactions=True):
            new_member = Member(name, age, comment)
            db.session.add(new_member)
        db.session.commit()
        return redirect(url_for('member_list'))
    return render_template('create_member.html', form=form)

@app.route('/update_member/<int:member_id>', methods=['GET', 'POST'])
def update_member(member_id):
    form = UpdateForm(request.form)
    member = Member.query.get(member_id)
    if request.method == 'POST' and form.validate():
        # メンバー更新
        id = form.id.data
        name = form.name.data
        age = form.age.data
        comment = form.comment.data
        with db.session.begin(subtransactions=True):
            member = Member.query.get(id)
            member.name = name
            member.age = age
            member.comment = comment
        db.session.commit()
        return redirect(url_for('member_list'))
    return render_template('update_member.html', form=form, member=member)

@app.route('/delete_member', methods=['GET','POST'])
def delete_member():
    form = DeleteForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.session.begin(subtransactions=True):
            id = form.id.data
            member = Member.query.get(id)
            db.session.delete(member)
        db.session.commit()
        return redirect(url_for('member_list'))
    return redirect(url_for('member_list'))

if __name__ == '__main__':
    app.run(debug=True)
