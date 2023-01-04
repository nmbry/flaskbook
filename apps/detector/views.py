from flask import Blueprint, render_template, send_from_directory, current_app

from apps import db
from apps.crud.models import User
from apps.detector.models import UserImage

detector = Blueprint(
    'detector',
    __name__,
    template_folder='templates',
)


@detector.route('/', methods=['GET'])
def index():
    user_images = (
        db.session.query(User, UserImage)
        .join(UserImage)
        .filter(User.id == UserImage.user_id)
        .all()
    )

    return render_template('detector/index.html', user_images=user_images)


@detector.route('/images/<path:filename>')
def image_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
