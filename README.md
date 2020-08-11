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