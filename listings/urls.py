from django.urls import path
from . import views             # chamada para a rota da view.

# /listings/23
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]