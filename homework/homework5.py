def check_admin(is_admin: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if is_admin:
                return func(*args, **kwargs)
            else:
                print("Доступ запрещён. Только для админов.")
        return wrapper
    return decorator


@check_admin(is_admin=True)
def delete_user():
    print("Пользователь удалён.")


@check_admin(is_admin=False)
def delete_post():
    print("Пост удалён.")


delete_user()
delete_post()
