from utils import validators


class Validator():

    @classmethod
    def validate_user(cls, user):
        from user.models import User
        return User.validate_registry(user, required=True)

    @classmethod
    def validate_pizza(cls, pizza):
        from pizza.models import Pizza
        return Pizza.validate_registry(pizza, required=True)
