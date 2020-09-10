from django.urls import path
from . import views             # chamada para a rota da view.

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]