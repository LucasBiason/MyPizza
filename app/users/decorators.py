from rest_framework.exceptions import PermissionDenied, NotAuthenticated


def administrator_required():
    """ User must be staff """
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated:
                if not user.is_staff and not user.is_superuser:
                    raise PermissionDenied('USER TYPE NOT ALLOWED')
                return func(request, *args, **kwargs)
            else:
                raise NotAuthenticated('NOT LOGGED USER')
        return wrapper
    return decorator


def superuser_required():
    """ User must be a Superuser """
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated:
                if not user.is_superuser:
                    raise PermissionDenied('USER TYPE NOT ALLOWED')
                return func(request, *args, **kwargs)
            else:
                raise NotAuthenticated('NOT LOGGED USER')
        return wrapper
    return decorator


def owner_required():
    """ User must be a Owner """
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated:
                if not user.is_staff and not user.is_superuser \
                   and not user.is_owner:
                    raise PermissionDenied('USER TYPE NOT ALLOWED')
                return func(request, *args, **kwargs)
            else:
                raise NotAuthenticated('NOT LOGGED USER')
        return wrapper
    return decorator
