from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('postlist', views.PostList.as_view()),
    path('postdetail/<str:pk>', views.PostDetail.as_view()),
    path('commentlist', views.CommentList.as_view()),
    path('commentdetail/<str:pk>', views.CommentDetail.as_view()),
    path('notificationlist', views.NotificationList.as_view()),
    path('notificationdetail/<str:pk>', views.NotificationDetail.as_view()),
    path('users', views.Users.as_view()),
    path('user/<str:pk>', views.User.as_view()), 
]


urlpatterns = format_suffix_patterns(urlpatterns)


'''
path('', views.index),
path('register', views.register, name='register'),
path('main', views.main, name='main'),
path('story/<str:pk>/', views.story, name='story'),
path('create_post', views.create_post, name='create_post'),
path('update_post/<str:pk>/', views.update_post, name='update_post'),
path('delete_post/<str:pk>/', views.delete_post, name='delete_post'),
path('profile/<str:pk>/', views.profile, name='profile'),
path('login', views.login, name='login'),'''