from datetime import datetime

from apps import db


class UserImage(db.Model):
    # テーブル名
    __tablename__ = 'user_images'

    # ID
    id = db.Column(db.Integer, primary_key=True)
    # ユーザID
    user_id = db.Column(db.String, db.ForeignKey('users.id'))
    # 画像パス
    image_path = db.Column(db.String)
    # 検知されたかどうか
    is_detected = db.Column(db.Boolean, default=False)
    # 作成日時
    created_at = db.Column(db.DateTime, default=datetime.now)
    # 更新日時
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
