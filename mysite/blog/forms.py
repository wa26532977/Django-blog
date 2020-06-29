from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("author", "title", "text")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            # class connect to css and bootstrap4
            'text': forms.Textarea(attrs={'class': "editable form-control medium-editor-textarea postcontent", 'id': "exampleFormControlTextarea1", "rows": "5"}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("author", "text")

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': "editable medium-editor-textarea"}),
        }
