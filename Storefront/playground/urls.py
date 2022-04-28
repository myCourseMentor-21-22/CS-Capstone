from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.my_information, name='info'),
    path('login/', views.log, name='log'),
    path('register/', views.register, name='register'),
    path('display_grades/', views.display_grades, name='display_grades'),
    path('edit/', views.edit, name='edit'),
    path('predict_prior/', views.predict_prior, name='predict_prior'),
    path('predict_next/', views.predict_next, name='predict_next'),
    path('predict_final/', views.predict_final, name='predict_final'),
    path('update_grades/', views.update_grades, name='update_grades'),
    path('testing/', views.testing, name='testing')
]