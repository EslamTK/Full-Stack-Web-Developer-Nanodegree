from functools import wraps

from core import *


def is_logged(token):
    if token:
        request_user = users.get_by_token(token=token)
        if request_user is not None:
            return True, request_user
        return False, None
    return False, None


def check_token(func):
    """Decorator Function to check the correctness of the user token cookie"""

    @wraps(func)
    def decorated(*args, **kwargs):
        token = kwargs['token']
        kwargs.pop('token')

        result = is_logged(token)
        return func(is_logged=result[0], request_user=result[1], *args, **kwargs)

    return decorated


def check_ownership(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = kwargs['token']
        kwargs.pop('token')

        result = is_logged(token)
        owner = False
        logged = result[0]
        request_user = result[1]
        request_blog = blogs.get_by_id(kwargs['blog_id'])

        if logged:
            owner = users.is_owner_of_blog(request_user, request_blog)

        return func(is_logged=logged, is_owner=owner, request_blog=request_blog, *args, **kwargs)

    return decorated
