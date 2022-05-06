from django.urls import path
from base import views
urlpatterns = [
    path('', views.home, name="home"),
    path('sign_up', views.sign_up, name="sign_up"),
]
