from flask import Flask
from flask_migrate import Migrate

from apps import db, csrf, login_manager
from apps.config import config


# 本では以下に宣言されているが、循環インポートになってしまうので誤りな気がする
# 公式Doc <https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/patterns/appfactories.html>
# db = SQLAlchemy()


def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(config[config_key])
    # app.config.from_mapping(
    #     SECRET_KEY='abcdefghijklmn',
    #     SQLALCHEMY_DATABASE_URI=f"sqlite:///{pathlib.Path(__file__).parent.parent / 'local.sqlite'}",
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False,
    #     SQLALCHEMY_ECHO=True,
    #     WTF_CSRF_SECRET_KEY='asdfghjkl',
    # )

    db.init_app(app)
    Migrate(app, db)

    csrf.init_app(app)

    login_manager.init_app(app)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix='/crud')

    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix='/auth')

    from apps.detector import views as detector_views
    app.register_blueprint(detector_views.detector, url_prefix='/')
    # app.register_blueprint(detector_views.detector)

    from apps.sample import controller as sample_controller
    # app.register_blueprint(sample_controller.sample, url_prefix='/sample')
    app.register_blueprint(sample_controller.sample, url_prefix='/sample')

    return app


if __name__ == '__main__':
    pass
