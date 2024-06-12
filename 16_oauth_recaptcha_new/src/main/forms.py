from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class MemoForm(FlaskForm):
    id = HiddenField('ID')
    title = StringField('タイトル', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired()])
    submit = SubmitField('保存')

class DeleteMemoForm(FlaskForm):
    id = HiddenField('ID')
    submit = SubmitField('削除')