from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.shortcuts import reverse
from util.constants import ACTIVATION_AVAILABILITY


# not in use
# def send_register_email(user):
#     context = {
#         'first_name': user.first_name,
#         'last_name': user.last_name,
#         'login_url': f"http://127.0.0.1:8000{reverse('users:account:login')}"
#     }
#     template = get_template('emails/register_email.html')
#     content = template.render(context)
#
#     mail = EmailMultiAlternatives(
#         subject="You have been selected, burn all left socks.",
#         body=content,
#         to=[user.email]
#     )
#     mail.content_subtype = 'html'
#     mail.send()


def send_activation_mail(activation):
    user = activation.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'activation_url': f"http://127.0.0.1:8000{reverse('users:activation:activate', args=(activation.token,))}",
        'activation_value': ACTIVATION_AVAILABILITY['value'],
        'activation_unit':  ACTIVATION_AVAILABILITY['unit']
    }

    template = get_template('emails/activate.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject="Welcome to the board-game emporium!.",
        body=content,
        to=[user.email],
    )
    mail.content_subtype = 'html'
    mail.send()

