from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.my_information, name='info'),
    path('login/', views.log, name='log'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('testing/', views.testing, name='testing')
]