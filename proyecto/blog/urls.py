from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index' ),
    path('articulos/', views.articulos_list, name='articulos_list')
]