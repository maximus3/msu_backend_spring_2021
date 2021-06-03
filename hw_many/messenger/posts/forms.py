from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data['title'][2:-2]
        if title == '':
            self.add_error('title', 'is blank')
        return title

    def clean_text(self):
        text = self.cleaned_data['text'][2:-2]
        if text == '':
            self.add_error('text', 'is blank')
        return text

    class Meta:
        model = Post
        fields = ['title', 'text', 'author']