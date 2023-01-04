from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from apps import db, login_manager


class User(db.Model, UserMixin):
    # テーブル名
    __tablename__ = 'users'

    # カラムを定義する
    # ID
    id = db.Column(db.Integer, primary_key=True)
    # ユーザ名
    username = db.Column(db.String, index=True)
    # メールアドレス
    email = db.Column(db.String, unique=True, index=True)
    # ハッシュ化されたパスワード
    password_hash = db.Column(db.String)
    # 作成日時
    created_at = db.Column(db.DateTime, default=datetime.now)
    # 更新日時
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError('読み取り不可')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # パスワードチェック
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # メールアドレス重複チェック
    def is_duplicate_email(self):
        print('====', db.session.query(User).filter_by(email=self.email).first())
        return db.session.query(User).filter_by(email=self.email).first() is not None

    # @classmethod
    def convert_from(cls, user_dict):
        user = User()
        user.id = user_dict.id
        user.username = user_dict.username
        user.email = user_dict.email
        user.password_hash = user_dict.password_hash
        user.created_at = user_dict.created_at
        user.updated_at = user_dict.updated_at

        return user


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
