from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    path('main', views.main, name='main'),
    path('story/<str:pk>/', views.story, name='story'),
    path('publish', views.publish, name='publish')
]