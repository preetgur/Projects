# Projects
1. Project Setup and Basic configration

    # Project directory
    >> django-admin startproject paytoservice

    # New App
    >> python manage.py startapp blog

    # Add the appname in settings.py

    INSTALLED_APPS = [ "blog" ]  or ["blog.apps.BlogConfig"]

    # urls and views configruations
    links the app urls with project urls

    # create "templates" folder inside blog inorder to use html files

2. Templates and Template Inheriting
3. Configuring static and media files
4. Install whitenoise for static files
    >> pip install whitenoise

    # Add to the Middleware
    >>'whitenoise.middleware.WhiteNoiseMiddleware'
5. Create Database
    # create Two model 
    Post | Tag    

    Register the modesl in admin.py
6. create a url and view method for accessing singel post and named the url in urls.py
7. Adding the image field
    >> thumbnail = models.ImageField(null=True,blank=True,upload_to="media")
    and uselike
    >> <img src=" {{post.thumbnail.url}}">
    
8. create a form of Post model in order to use curd.
    # adding the checkbox to manytomany fields in forms.py    
    >> widgets = {

            'tags': forms.CheckboxSelectMultiple(),
        }

9. In order to add image to post we have to use enctype="multipart/form-data"
    >>  <form action="" method ="post" enctype="multipart/form-data">

    in order to save the image to database we have to do as :
    >> form = PostForm(request.POST,request.FILES)