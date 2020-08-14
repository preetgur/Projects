from django.shortcuts import render
from .models import Post,Tag
# Create your views here.

def home(request):

    return render(request,"blog/home.html")


# single post

def post(request,pk):
    
    context = {
        'post':Post.objects.get(id = pk)
    }

    return render(request,"blog/post.html",context)

# All post
def posts(request):
    context = { 
        'posts':Post.objects.filter(active=True)
    }
    return render(request,"blog/posts.html",context) 
       