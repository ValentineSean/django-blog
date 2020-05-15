from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_delete/<int:pk>', views.post_delete), #to be done also
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # To be done!!!
    path('', include('django.contrib.auth.urls')),
]