

"""bg_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import homepage_view, contact_view, sell_view, about_us_view, payment_and_delivery
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


# admin.site.urls
urlpatterns = [
    # path('admin/import/', AdminImport.get_urls ,name='import'),
    path('admin/', admin.site.urls, name='admin'),
    path('about_us/', about_us_view, name='about_us'),
    path('payment_delivery/', payment_and_delivery, name='payment_delivery'),
    path('', homepage_view),
    path("contact/", contact_view, name='contact'),
    path("sell/", sell_view),
    path('users/', include('users.urls')),
    path('products/', include('products_stock.urls')),
    path('payments/', include('payments.urls')),
    path('orders/', include('orders.urls')),
    path('images/favicon.ico',
         RedirectView.as_view(url=staticfiles_storage.url(
             'images/favicon.ico')))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
