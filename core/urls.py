from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [ 
    path('', views.index),
    path('register', views.register, name='register'),
    path('main', views.main, name='main'),
    path('story/<str:pk>/', views.story, name='story'),
    path('create_post', views.create_post, name='create_post'),
    path('update_post/<str:pk>/', views.update_post, name='update_post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete_post'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('postlist', views.PostList.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)