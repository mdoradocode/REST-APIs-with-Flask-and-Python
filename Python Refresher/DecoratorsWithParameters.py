import functools
user = {"username": "jose", "access_level": "admin"}


def make_secure(access_level):
    def decorator(func):
        ##Keeps the name of the original function
        @functools.wraps(func)
        ##Make the internal function take in unlimited numbers of arguements with kwargs and args
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)

        return secure_function
    return decorator

@make_secure("admin")
def get_password():
    return "admin: 1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_dashboard_password())
print(get_password())