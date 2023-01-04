import pathlib

basedir = pathlib.Path(__file__).parent.parent


# 共通の設定項目
class BasicConfig(object):
    SECRET_KEY = 'abcdefghijklmn'
    WTF_CSRF_SECRET_KEY = 'asdfghjkl'
    UPLOAD_FOLDER = str(pathlib.Path(basedir, 'apps', 'images'))


# ローカル環境の設定項目
class LocalConfig(BasicConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# テスト環境の設定項目
class TestingConfig(BasicConfig):
    # SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


config = {
    'local': LocalConfig,
    'testing': TestingConfig,
}
