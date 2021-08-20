import secrets
from django.db import models
from bg_store.models import CustomModel
from django.conf import settings
from django.utils import timezone
from util.constants import ACTIVATION_AVAILABILITY_DICT


class Activation(CustomModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    token = models.CharField(max_length=64, default=secrets.token_hex(32))
    expires_at = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(
            **ACTIVATION_AVAILABILITY_DICT
        )
    )

    activated_at = models.DateTimeField(null=True, default=None)
