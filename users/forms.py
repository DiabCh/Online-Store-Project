from django import forms
from users.models import Address
from django.contrib.auth.password_validation import validate_password, \
    password_validators_help_text_html
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from util.constants import SHIPPING_ADDRESS, BILLING_ADDRESS
from django.db import models

AuthUser = get_user_model()


# Register form for user initial register, asks for fname,
# lname and email and saves them to db
class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']

# commit = False is to create an object to which you can add more data
    def save(self, commit=True):
        email = self.cleaned_data['email']

        self.instance.username = email
        return super().save(commit)


# Once redirected from the email, this form is to activate account and confirm
# password through an authentication token.
class UserActivation(forms.Form):
    # form model
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,
                               required=True,
                               help_text=password_validators_help_text_html()
                               )
    password_confirmation = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        required=True
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args,
                         **kwargs)  # this calls the mother
        # __init__ and initializes it too
        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # validates password to check for length, numbers, etc
        validate_password(password, self.user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError("the passwords do not match.")

        return password_confirmation

    def save(self, commit=True):
        # print('here')
        # print(self.user.is_active)

        self.user.set_password(self.cleaned_data.get('password'))
        self.user.is_active = True
        # print(self.user.is_active)
        self.user.save()


# removes passwords from user creation in admin
class UserCreationForm(BaseUserCreationForm):

    password1 = None
    password2 = None

    def save(self, commit=True):
        user = super(BaseUserCreationForm, self).save(commit=False)
        # super()
        # will use the save feature within BaseUser
        # creation, super(BaseUserCreation) will
        # use the one within it's father located in forms.ModelForm
        if commit:
            user.save()
        return user


class AddressType(models.TextChoices):
    SHIPPING = SHIPPING_ADDRESS
    BILLING = BILLING_ADDRESS


class SectorChoices(models.TextChoices):
    SECTOR_1 = '1', 'Sector 1'
    SECTOR_2 = '2', 'Sector 2'
    SECTOR_3 = '3', 'Sector 3'
    SECTOR_4 = '4', 'Sector 4'
    SECTOR_5 = '5', 'Sector 5'
    SECTOR_6 = '6', 'Sector 6'


class AddressForm(forms.Form):
    country = forms.CharField(
        max_length=255,
        required=True,
    )
    city = forms.CharField(
        max_length=255,
        required=True
    )
    sector = forms.ChoiceField(
        choices=SectorChoices.choices,
        required=True
    )
    street = forms.CharField(
        max_length=255,
        required=True
    )
    building = forms.CharField(
        max_length=255,
        required=True
    )
    floor = forms.CharField(
        max_length=255,
        required=True
    )
    apartment = forms.CharField(
        max_length=10,
        required=True
    )

    type = forms.MultipleChoiceField(
        choices=AddressType.choices,
        required=True,
        label='address type'
    )

    def clean_address_data(self, user):
        country = self.cleaned_data.get('country')
        city = self.cleaned_data.get('city')
        sector = self.cleaned_data.get('sector')
        street = self.cleaned_data.get('street')
        building = self.cleaned_data.get('building')
        floor = self.cleaned_data.get('floor')
        apartment = self.cleaned_data.get('apartment')
        type = self.cleaned_data.get('type')

        Address(
            user=user,
            country=country,
            city=city,
            sector=sector,
            street=street,
            building=building,
            floor=floor,
            appartment=apartment,
            type=type[0],
        ).save()
