from django.urls import path
from . import views


urlpatterns = [
    path('job/', views.post_job, name='Job Posting'),
    path('job/<str:pk>/', views.job_detail, name='Job details'),
    path('jobs/', views.job_list, name='Job listings'),
    path('jobs/find/', views.filter, name='Job Filter'),
]
