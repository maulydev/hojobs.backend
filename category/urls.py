from django.urls import path
from .views import categories


urlpatterns = [
    path('categories/', view=categories, name='Job Categories')
]
