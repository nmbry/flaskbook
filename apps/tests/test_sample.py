from apps.sample.models import my_func


def test_select_by_user_id(fixture_app):
    result = my_func(100)

    for row in result:
        assert row['id'] == 100
        assert row['username'] == 'test100'
        assert row['email'] == '100@test.com'
        assert row['password_hash'] == 'pw100'
