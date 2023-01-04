# app.pyに宣言すると以下のエラーが発生するので、初期化のタイミングでグローバルに宣言する
# ImportError: cannot import name 'db' from partially initialized module 'apps.app'
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# DBの初期化
db = SQLAlchemy()

# CSRFの初期化
csrf = CSRFProtect()

# LoginManagerの初期化
login_manager = LoginManager()
# 未ログイン時のリダイレクト先のエンドポイント
login_manager.login_view = 'auth.signup'
# ログイン後に表示されるメッセージを空にする（指定しないと英語が出力されるため）
login_manager.login_message = ''
