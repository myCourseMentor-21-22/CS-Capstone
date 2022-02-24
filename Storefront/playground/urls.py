from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.my_information, name='info'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('display_grades/', views.display_grades, name='display_grades')
]