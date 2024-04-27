from . import views
from django.urls import path

urlpatterns = [
    path('login', views.user_login),
    # path('',views.home),
    path('signup',views.user_signup)
]

