# from views import *
from django.urls import path, include 
from blog import views 
# from views import * 

    
# Page           --   URL	                 --  * Description  *
# Homepage	     --    /	                 --   Shows latest blog posts
# Post Detail	 --   /post/<id>/	         --   Displays a single post with comments
# Create Post	 --   /create/	             --   Form for creating a new post
# Author Profile --   /author/<username>/	 --   Displays an author's profile and posts
# Tagged Posts	 --   /tag/<tagname>/	     --   Shows all posts with a specific tag


urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('posts/', views.post_detail, name='post_detail'),
    path('posts/add/', views.post_form, name='post_add'),
    path('posts/edit/<int:id>/', views.post_form, name='post_update'),
    path('author/profile', views.author_profile, name='author_profile'),
    path('posts/taggged/', views.tagged_post, name='tagged_post')

]