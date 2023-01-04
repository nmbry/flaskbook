from apps import db


def my_func(user_id):
    result = db.session.execute(
        f"""
        SELECT * FROM users WHERE id={user_id}
        """
    )

    return result
