from django.urls import path
from .views import subscriber, unsubscriber, resubscriber


urlpatterns = [
    path('subscribe/', view=subscriber, name='Add subscription'),
    path('resubscribe/', view=resubscriber, name='Renew subscription'),
    path('unsubscribe/', view=unsubscriber, name='Remove subscription')
]
