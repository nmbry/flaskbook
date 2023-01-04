from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms import SubmitField


class UploadImageForm(FlaskForm):
    image = FileField(
        validators=[
            FileRequired('画像ファイルを指定してください。'),
            FileAllowed(['png', 'jpg', 'jpeg'], 'サポートされていない画像形式です。'),
        ],
    )

    submit = SubmitField('アップロード')
