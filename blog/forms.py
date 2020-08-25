from django import forms
from .models import Post

# Post form

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"

        widgets = {

            'tags': forms.CheckboxSelectMultiple(), # adding checkbox to manytomany relationship
        }