import secrets
from django.utils import timezone
from django.shortcuts import HttpResponse, render, redirect
from django.utils.decorators import decorator_from_middleware
from users.middleware.activation import ValidateTokenMiddleware
from users.models import Activation
from users.emails import send_activation_mail
from util.constants import ACTIVATION_AVAILABILITY_DICT
from users.forms import UserActivation
from django.contrib.auth import login, authenticate


@decorator_from_middleware(ValidateTokenMiddleware)
def activate_view(request, token):
    # gets the activation entry in the db based on the token received.
    activation = Activation.objects.get(token=token) # activation.user

    if request.method == 'GET':
        form = UserActivation(activation.user)
    else:
        form = UserActivation(activation.user, request.POST)

        if form.is_valid():

            form.save()
            # Log-in user
            email = activation.user.email
            password = form.cleaned_data.get('password')
            authenticated_user = authenticate(request,
                                              username=email,
                                              password=password)

            if authenticated_user is not None:
                login(request, authenticated_user)

            return redirect('/')

        return redirect('/')

    return render(request, 'activation/activate.html', {
       'token': token,
       'form': form
   })


@decorator_from_middleware(ValidateTokenMiddleware)
def reset_token(request, token):
    if request.method == 'GET':
        return render(request, 'activation/reset_token.html', {
            'token': token
        })
    # reset token
    activation = Activation.objects.get(token=token)
    activation.token = secrets.token_hex(32)
    activation.expires_at = timezone.now() + timezone.timedelta(**ACTIVATION_AVAILABILITY_DICT)
    activation.save()

    send_activation_mail(activation)
    return redirect('/') # can add a redirect message ergo 'your activation token has been reset, check mail'
