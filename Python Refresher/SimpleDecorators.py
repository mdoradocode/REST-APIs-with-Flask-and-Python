user = {"username": "jose", "access_level": "admin"}


def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function

##This line calls the make_secure function, which defines the secure function and returns the secure_function function. Then get_admin_password is set to secure_function. So in line 16 when get_admin_password is called, you actually call make_secure which returns get_admin_password through the key word func
get_admin_password = make_secure(get_admin_password)
print(get_admin_password())