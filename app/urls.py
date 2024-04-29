from django.urls import path
from django.http import HttpResponse
from app import views



urlpatterns = [
    path('', views.job_list, name="jobs_home"),
    path('job/<int:id>/', views.job_detail, name='jobs_detail'),
]
