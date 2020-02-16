from django.urls import path
from . import views
urlpatterns = [
    path('', views.point_list, name = 'post_list'),
]