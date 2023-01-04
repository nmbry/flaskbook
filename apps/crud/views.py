from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required

from apps import db
from apps.crud.forms import UserForm
from apps.crud.models import User

crud = Blueprint(
    'crud',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@crud.route('/', methods=['GET'])
@login_required
def index():
    return render_template('crud/index.html')


@crud.route('/users', methods=['GET'])
@login_required
def users():
    query = f"-- SELECT * FROM users;"
    users_list = db.session.query(User).all()
    # users_list = db.session.execute(query)

    return render_template('crud/index.html', users=users_list)


@crud.route('/users/create', methods=['GET', 'POST'])
@login_required
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        db.session.add(user)
        db.session.commit()

        # ユーザ一覧画面へリダイレクトする
        return redirect(url_for('crud.users'))

    return render_template('crud/create.html', form=form)


@crud.route('/users/<user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    form = UserForm()
    # TODO: 生のSQLを実行する場合は別クラスにtable_mapperとquery_mapperをまとめておく必要がある
    # TODO: また、自前でDBを設計してヘビーにsqlAlchemyを利用せず、ライトに利用するようにした方がよい
    # query = f"""
    # SELECT
    #     id,
    #     username,
    #     email,
    #     password_hash,
    #     created_at,
    #     updated_at
    # FROM users
    # WHERE id={user_id} ;
    # """
    # user_dict = db.session.execute(query).mappings().first()
    # user = User.convert_from(user_dict)
    # print('========1', user.id, user.email, user.created_at, user.updated_at)

    user = db.session.query(User).filter_by(id=user_id).first()

    if form.validate_on_submit():
        # TODO: 生のSQLを実行する場合は別クラスにtable_mapperとquery_mapperをまとめておく必要がある
        # TODO: また、自前でDBを設計してヘビーにsqlAlchemyを利用せず、ライトに利用するようにした方がよい
        # query = f"""
        # UPDATE users
        # SET
        #     username={user.username},
        #     email={user.email},
        #     password_hash={user.password_hash},
        #     created_at={user.created_at},
        #     updated_at={datetime.now}
        # WHERE id={user.user_id}
        # """
        # db.session.execute(query)
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data

        db.session.add(user)
        db.session.commit()

        # ユーザ一覧画面へリダイレクトする
        return redirect(url_for('crud.users'))

    return render_template('crud/edit.html', user=user, form=form)


@crud.route('/users/<user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()

    # ユーザ一覧画面へリダイレクトする
    return redirect(url_for('crud.users'))
