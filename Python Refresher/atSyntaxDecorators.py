import functools
user = {"username": "jose", "access_level": "admin"}

##This replaces line 20, now the get_admin_password is replaced by secure_function
##make_secure is the decarator while secure_function is just a function
def make_secure(func):
    ##Keeps the name of the original function (get_admin_secure)
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function
    
@make_secure
def get_admin_password():
    return "1234"

#!This line calls the make_secure function, which defines the secure function and returns the secure_function function. Then get_admin_password is set to secure_function. So in line 16 when get_admin_password is called, you actually call make_secure which returns get_admin_password through the key word func
#!get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
print(get_admin_password.__name__)