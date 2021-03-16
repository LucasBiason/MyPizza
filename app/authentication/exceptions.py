from rest_framework.exceptions import AuthenticationFailed


def raise_invalid_token():
    raise AuthenticationFailed('Invalid Token')


def raise_expired_token():
    raise AuthenticationFailed('Expired Token')


def raise_user_not_active():
    raise AuthenticationFailed('User is not active')
