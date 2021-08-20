from django.urls import path
from .views import list_cards, add_card, remove_card, process_payment, failed_process, process_3d_secure
from django.conf.urls import url
app_name = 'payments'

urlpatterns = [
    path('cards/', list_cards, name='list_cards'),
    path('cards/add/', add_card, name='add_card'),
    path('cards/<str:stripe_card_id>/remove', remove_card, name='remove_card'),
    path('process/<str:card_id>', process_payment, name='process'),
    path('process/3d_secure/', process_3d_secure, name='3d_secure'),
    path('process/failed/', failed_process, name='failed'),
]