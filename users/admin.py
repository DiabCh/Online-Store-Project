from users.models import AuthUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from users.forms import UserCreationForm
from django.urls import path


# we inherent BaseUserAdmin in order to rewrite ordering to no longer
# require username but instead email
@admin.register(AuthUser)
class AuthUserAdmin(BaseUserAdmin):
    # what to list in the user display
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    # order by
    ordering = ('email',)
    # user fields
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # fields when adding a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )
    # we can search by :
    search_fields = ('first_name', 'last_name', 'email')
    add_form = UserCreationForm

    def get_urls(self):
        # this rewrites and removes the code that enables
        # site/admin/<id>/password to lead to a password change setting
        return super(BaseUserAdmin, self).get_urls()
