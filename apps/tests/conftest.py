import pytest

from apps import db
from apps.app import create_app

"""
テスト関数の前後に処理を実行するフィクスチャという機能がある。

tests/conftest.pyにフィクスチャを作成することで、
testsパッケージ配下の全てのテストでフィクスチャを使用することが可能となる。
　※複数階層からでも呼べる
"""

dummy_data = [
    {'id': 100, 'username': 'test100', 'email': '100@test.com', 'password_hash': 'pw100'},
    {'id': 101, 'username': 'test101', 'email': '101@test.com', 'password_hash': 'pw101'},
    {'id': 102, 'username': 'test102', 'email': '102@test.com', 'password_hash': 'pw102'},
    {'id': 103, 'username': 'test103', 'email': '103@test.com', 'password_hash': 'pw103'},
    {'id': 104, 'username': 'test104', 'email': '104@test.com', 'password_hash': 'pw104'},
    {'id': 105, 'username': 'test105', 'email': '105@test.com', 'password_hash': 'pw105'},
]


def insert_dummy_data():
    for data in dummy_data:
        db.session.execute(
            f"""
            INSERT INTO users (id, username, email, password_hash, created_at, updated_at)
            VALUES ({data['id']}, '{data['username']}', '{data['email']}', '{data['password_hash']}', null, null);
            """
        )


def delete_dummy_data():
    for data in dummy_data:
        db.session.execute(
            f"""
            DELETE FROM users WHERE id={data['id']};
            """
        )


@pytest.fixture
def fixture_app():
    # テスト用のDBを利用する
    app = create_app('testing')
    app.app_context().push()

    # テストデータをINSERTする
    insert_dummy_data()

    # テストを実行する
    yield app

    # テストデータをDELETEする
    delete_dummy_data()

    # コミットする
    db.session.commit()
