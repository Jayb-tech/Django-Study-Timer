from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('start/', views.start_study_timer, name='start_study_timer'),
    path('stop/', views.stop_study_timer, name='stop_study_timer'),  # Fix: was using start_study_timer
    path('', views.study_timer, name='study_timer'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]