from django.urls import path, include
from . import views 

urlpatterns = [

    path('', views.index),
    path('register', views.register, name='register'),
    path('main', views.main, name='main'),
    path('notification', views.notification, name='notification'),
    path('story/<str:pk>/', views.story, name='story'),
    path('create_post', views.create_post, name='create_post'),
    path('update_post/<str:pk>/', views.update_post, name='update_post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete_post'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('del_comment/<str:pk>', views.del_comment, name='del_comment'),
    path('edit_profile/<str:pk>', views.edit_profile)
    ]

 