from django.urls import path
from . import views


urlpatterns = [
    path('employer/verify/', views.verify_employer, name='Verify Employer'),
]
