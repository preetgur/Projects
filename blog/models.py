from django.db import models

# Create your models here.



class Post(models.Model):

    headline = models.CharField(max_length=200,null=True,blank=True)
    sub_headline = models.CharField(max_length=200,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    published_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = False)

    tags = models.ManyToManyField('Tag',blank=True)
    #slugs =
    


    def __str__(self):
        return self.headline


class Tag(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name