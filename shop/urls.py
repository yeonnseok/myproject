from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index, name='index'),
]