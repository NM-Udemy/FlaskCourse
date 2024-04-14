from app import app
from flask import render_template, request, url_for, redirect
from models import db, Member
from forms import CreateForm, DeleteForm, UpdateForm


@app.route('/')
@app.route('/member_list')
def member_list():
    members = db.session.execute(db.Select(
        Member.id, Member.name, Member.age, Member.comment
    )).all()
    delete_form = DeleteForm()
    return render_template(
        'member_list.html', members=members, delete_form=delete_form
    )

@app.route('/create_member', methods=['GET', 'POST'])
def create_member():
    form = CreateForm(request.form)
    if request.method=="POST" and form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        comment = form.comment.data
        new_member = Member(name=name, age=age, comment=comment)
        db.session.add(new_member)
        db.session.commit()
        return redirect(url_for('member_list'))
    return render_template('create_member.html', form=form)

@app.route('/update_member/<int:member_id>', methods=["GET", "POST"])
def update_member(member_id):
    form = UpdateForm(request.form)
    member = Member.query.get_or_404(member_id)
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        comment = form.comment.data
        member.name = name
        member.age = age
        member.comment = comment
        db.session.commit()
        return redirect(url_for('member_list'))
    form.comment.data = member.comment
    return render_template('update_member.html', member=member, form=form)

@app.route('/delete_member', methods=["POST",])
def delete_member():
    form = DeleteForm(request.form)
    if form.validate_on_submit():
        id = form.id.data
        member = Member.query.get_or_404(id)
        db.session.delete(member)
        db.session.commit()
    return redirect(url_for('member_list')) 

if __name__ == '__main__':
    app.run(debug=True)
