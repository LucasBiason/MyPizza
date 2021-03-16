from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.models import Site
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings

from django_rest_passwordreset.signals import reset_password_token_created

from .emails import message, subject


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token,
                                 *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    site = Site.objects.get_current()
    path = reverse('password_reset:reset-password-request')

    context = {
        'site_name': f"Password Reset for {site.name}",
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': f"{site.domain}{path}?token={reset_password_token.key}"
    }
    context_message = set_email_context(message, context)

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [reset_password_token.user.email,]

    msg = EmailMultiAlternatives(
       subject, context_message, email_from, recipient_list
    )
    msg.attach_alternative(context_message, "text/html")
    msg.send()


def set_email_context(context_message, context):
        for key, value in context.items():
            context_message = context_message.replace(f"[[{key}]]", str(value))
        return context_message
