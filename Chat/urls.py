from django.urls import path
from .import views

#app_name = 'Chat'

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<str:pk>/', views.detail, name="detail"),
    path('send/<str:pk>/', views.SendMessages, name="send_msg"),
]