from django.urls import path
from api import views

urlpatterns = [
    path('home/', views.home),
    path('api/broker/login/fyers/', views.fyers_login),
    path('api/getprofile/', views.get_user_profile)
]
