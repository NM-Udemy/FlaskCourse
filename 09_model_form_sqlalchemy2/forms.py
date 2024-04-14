from flask_wtf import FlaskForm
from wtforms import (
    HiddenField, StringField, IntegerField, TextAreaField,
    SubmitField
)
from wtforms.validators import DataRequired, NumberRange

class CreateForm(FlaskForm):
    name = StringField('名前は:', validators=[DataRequired()])
    age = IntegerField(
        '年齢は:', validators=[DataRequired(), NumberRange(min=0, max=150)]
    )
    comment = TextAreaField('コメント:')
    submit = SubmitField('作成')

class UpdateForm(FlaskForm):
    name = StringField('名前は:', validators=[DataRequired()])
    age = IntegerField(
        '年齢は:', validators=[DataRequired(), NumberRange(min=0, max=150)]
    )
    comment = TextAreaField('コメント:')
    submit = SubmitField('更新')


class DeleteForm(FlaskForm):
    id = HiddenField()
    submit = SubmitField('削除')