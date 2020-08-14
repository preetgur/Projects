from django.shortcuts import render,redirect
from .models import Post,Tag
from .forms import PostForm
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
       
# curd 

def createPost(request):

    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
     
            return redirect('posts')

    context = { 'form':form}
    return render(request,"blog/createPost.html",context)    