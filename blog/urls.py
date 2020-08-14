from django.urls import path
from . import views


urlpatterns = [
    path("",views.home),
    path("post/<str:pk>",views.post,name='post'),
    path("posts",views.posts,name='posts'),

    # curd
    path("createPost",views.createPost,name="createPost"),
]