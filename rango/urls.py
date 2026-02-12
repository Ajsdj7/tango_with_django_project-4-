from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<category_name_slug>/', views.show_category, name='show_category'),
    path('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
]