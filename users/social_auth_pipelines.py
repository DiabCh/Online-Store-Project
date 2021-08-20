import requests
from django.core.files.base import ContentFile
import secrets

USER_FIELDS = ['username', 'email', 'first_name', 'last_name']


def create_user(strategy, details, backend, user=None, **kwargs):
    if user:
        return {'is_new': False}

    fields = dict(
        (name, kwargs.get(name, details.get(name)))
        for name in backend.setting('USER_FIELDS', USER_FIELDS)
    )

    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields, is_social_auth=True)
    }


def get_profile_picture(backend, user, response, is_new, *args, **kwargs):
    url = None
    params = {}

    if backend.name == 'google-oauth2':
        url = response.get('picture')
        # urls = response['picture'] this will produce an error
        # if an image is not retrieved
    elif backend.name == 'facebook':
        url = 'https://graph.facebook.com/%s/picture?access_token=%s' % (
              response['id'],
              response['access_token']
              )
        params['type'] = 'large'

    if url:
        try:
            image_response = requests.request('get', url, params=params)
            image_response.raise_for_status()
        except requests.HTTPError:
            pass
        else:
            # print('image response', image_response)
            image_content = image_response.content
            # print('image content', image_content)
            profile = user.profile
            profile.avatar.save('%s.jpg' % secrets.token_hex(32), ContentFile(image_content))
            profile.save()
