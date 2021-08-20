from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils import timezone
from users.models import Activation


class ValidateTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        # obtain token
        token = view_kwargs.get('token')
        # attempt to retrieve activation object based on token where
        # Activated_at is null due to not being activated
        activation = get_object_or_404(Activation, token=token, activated_at=None)
        reset_token_route = reverse('users:activation:reset_token', args=(token,))
        activate_route = reverse('users:activation:activate', args=(token,))
        # This returns as is_reset_token_route = True
        # if we are currently on the reset token path
        is_reset_token_route = request.path == reset_token_route

        # check if token is expired
        if activation.expires_at < timezone.now():
            if not is_reset_token_route:
                return redirect(reset_token_route)
            elif is_reset_token_route:
                return None

        if is_reset_token_route:
            return redirect(activate_route)
        # print('do something before processing view', request.path, token)


