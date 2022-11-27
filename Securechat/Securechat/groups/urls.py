from django.urls import path

from . import views

urlpatterns = [
    path('', views.groups, name='groups'),
    path('<slug:slug>/', views.group, name='group'),
]