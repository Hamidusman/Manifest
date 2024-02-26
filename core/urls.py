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

 
<nav class=" navbar  navbar-expand-lg fixed-top">
        <div class="d-flex w-100 justify-content-between align-items-center">
            
            <div class="collapse navbar-collapse" id="navigationMenu">
                <div class="layer1 d-flex flex-column justify-content-between mt-1 ">
            

                    <article class="navigation mt-3">
                        
                        <div class="mt-3     search-div d-flex justify-content-center align-items-center">
                                
                            <input type="search" name="" class="search" placeholder="Search" id="">
                        </div>
                
                        <a href="" class="navi-link mt-3 link-no-underline">
                            <div class="nav-container d-flex"> <!-- <a href="https://iconscout.com/icons/home" class="text-underline font-size-sm" target="_blank">Home</a> by <a href="https://iconscout.com/contributors/boosticon" class="text-underline font-size-sm">Haca Studio</a> on <a href="https://iconscout.com" class="text-underline font-size-sm">IconScout</a>-->
                                <img class="nav-icon" src="{% static 'img\home.svg' %}" alt="">
                                <h6 class="nav-title">Home</h6>
                            </div>
                        </a>
                        
                        <a href="" class="navi-link link-no-underline">
                            <div class="nav-container d-flex"> <!-- <a href="https://iconscout.com/icons/plus" class="text-underline font-size-sm" target="_blank">plus</a> by <a href="https://iconscout.com/contributors/piqodesign" class="text-underline font-size-sm">Piqo Design</a> on <a href="https://iconscout.com" class="text-underline font-size-sm">IconScout</a>-->
                                <img class="nav-icon" src="{% static 'img\create.svg' %}" alt="">
                                <h6 class="nav-title">Publish Post</h6>
                            </div>
                        </a>
                        
                        <a href="" class="navi-link link-no-underline">
                            <div class="nav-container d-flex"> <!--<a href="https://iconscout.com/icons/notification" class="text-underline font-size-sm" target="_blank">Notification</a> by <a href="https://iconscout.com/contributors/rengised" class="text-underline font-size-sm" target="_blank">Alex Martynov</a>-->
                                <img class="nav-icon" src="{% static 'img\noti.svg' %}" alt="">
                                <h6 class="nav-title">Notifications</h6>
                            </div>
                        </a>
                        
                        <a href="" class="navi-link link-no-underline">
                            <div class="nav-container d-flex"> <!-- <a href="https://iconscout.com/icons/category" class="text-underline font-size-sm" target="_blank">category</a> on <a href="https://iconscout.com" class="text-underline font-size-sm">IconScout</a>-->
                                <img class="nav-icon" src="{% static 'img\categories.svg' %}" alt="">
                                <h6 class="nav-title">Categories</h6>
                            </div>
                
                    </article>
                    
                    
                    <a href="" class="navi-link link-no-underline">
                        <div class="nav-container d-flex"> <!-- <a href="https://iconscout.com/icons/plus" class="text-underline font-size-sm" target="_blank">plus</a> by <a href="https://iconscout.com/contributors/piqodesign" class="text-underline font-size-sm">Piqo Design</a> on <a href="https://iconscout.com" class="text-underline font-size-sm">IconScout</a>-->
                            <img src="{% static 'img\log-in.svg' %}" alt="" class="nav-icon"> <!-- <a href="https://iconscout.com/icons/log-in" class="text-underline font-size-sm" target="_blank">log in</a> by <a href="https://iconscout.com/contributors/irfansusanto98" class="text-underline font-size-sm" target="_blank">Barudak Lier</a> -->
                            <h6 class="nav-title">Log In</h6>
                        </div>
                    </a>
                </div>
        

        
    </nav>