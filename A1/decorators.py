from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(veiw_func):
    def wrapper_fun(request , *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return veiw_func(request , *args , **kwargs)
    return wrapper_fun

def allowed_users(allowed_roles=[]):
    def decorator(view_fun):
        def wrapper_fun(request , *args , **kwargs):
            print('working', allowed_roles)
            return view_fun(request , *args , **kwargs)
        return wrapper_fun
    return decorator
