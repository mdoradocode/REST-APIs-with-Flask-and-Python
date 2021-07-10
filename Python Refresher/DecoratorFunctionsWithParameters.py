import functools
user = {"username": "jose", "access_level": "admin"}

##make_secure is the decarator while secure_function is just a function
def make_secure(func):
    ##Keeps the name of the original function (get_admin_secure)
    @functools.wraps(func)
    ##Make the internal function take in unlimited numbers of arguements with kwargs and args
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)

    return secure_function
    
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "password1"

print(get_password("billing"))
print(get_password.__name__)