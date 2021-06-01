from  .models import *
from django import  forms

class PostCreatioForm(forms.ModelForm):


    class  Meta:
        model = Post

        widgets = {
            'title':forms.TextInput(attrs={'class':'single-input','placeholder':'Enter your title'}),
            'content':forms.Textarea(attrs={'class':'single-input','placeholder':'Enter your content'}),

        }


        fields=[
            'title', 
            'content',
            'image',
            'category',
            'tag'
        ]