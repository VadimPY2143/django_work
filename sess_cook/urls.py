from django.urls import path
from sess_cook import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cache/', views.cache_test, name='cache')
]
