from django.urls import path
from . import views

#app_name ='posts'

urlpatterns = [
    path('', views.posts_list, name="posts"),
    path('<slug:slug>', views.post_page, name="post_page"),
]
