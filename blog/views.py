from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,"blog/home.html")


# single post

def post(request):

    return render(request,"blog/post.html")

# All post
def posts(request):

    return render(request,"blog/posts.html") 
       