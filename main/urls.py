from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_list, name='add_list'),
    path('<int:pk>/edit', views.edit_list, name='edit_list'),
    path('<int:pk>/delete', views.delete_list, name='delete_list'),
]