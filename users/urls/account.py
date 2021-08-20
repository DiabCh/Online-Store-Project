from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.account import register_view, notifications_view,\
    mark_notification_as_seen, profile_view, order_history_view,\
    order_details_view, change_password, add_address, view_addresses,\
    remove_address
from django.conf import settings
from django.conf.urls.static import static

# users:account
app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html')
         ),
    path('', include('django.contrib.auth.urls')),
    path('register/', register_view, name='register'),
    path('social-auth/', include('social_django.urls')),
    path('notifications/', notifications_view, name='notifications'),
    path('notifications/mark-as-seen/<int:notification_id>/', mark_notification_as_seen, name='notifications_mark_as_seen'),
    path('my_profile/', profile_view, name='profile'),
    path('order_history/', order_history_view, name='order_history'),
    path('order_history/order_details/<int:order_id>/', order_details_view, name='order_details'),
    path('password/', change_password, name='change_password'),
    path('addresses/view_addresses/', view_addresses, name='address_view'),
    path('addresses/add_address/', add_address, name='add_address'),
    path('addresses/remove_address/<int:address_id>', remove_address, name='remove_address')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)