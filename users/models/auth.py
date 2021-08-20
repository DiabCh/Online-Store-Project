from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# We interact with AuthUser through AuthUserManager

class AuthUserManager(BaseUserManager):
    def create_user(self,
                    first_name,
                    last_name,
                    email,
                    is_social_auth=False
                    ):

        if not first_name:
            raise ValueError('First name is required')

        if not last_name:
            raise ValueError('Last name is required')

        if not email:
            raise ValueError('Email is required')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,

        )
        user.is_social_auth = is_social_auth
        # user.is_social_auth is not defined in the model and cannot be
        # added to the constructor but we can add new attributes without
        # having to modify the user model.
        user.save()

        return user

    def create_superuser(
            self,
            first_name,
            last_name,
            email
    ):

        user = self.create_user(
            first_name,
            last_name,
            email
        )

        user.is_staff = True
        user.is_superuser = True
        user.username = None

        user.save()

        return user


# Base Auth User model can either inherent AbstractUser for django's base
# settings or BaseAbstractUser to be written from the ground up.
class AuthUser(AbstractUser):
    username = None
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=150,
        null=False
    )

    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=150,
        null=False
    )

    email = models.EmailField(
        verbose_name=_('email address'),
        null=False,
        unique=True
    )

    password = models.CharField(
        verbose_name=_('password'),
        max_length=128,
        null=True,
    )

    # is_active = models.BooleanField(
    #     _('active'),
    #     default=False,
    # )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__()

