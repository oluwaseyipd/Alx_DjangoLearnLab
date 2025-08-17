from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Comment, Tag, Post
from taggit.forms import TagWidget 


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()


    class Meta:
        model = User
        fields = [  'first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'gender', 'age', 'address', 'bio', 'profile_image', 'banner_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
        }

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Add comma-separated tags")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            'tags': TagWidget(),  
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            tags_str = self.cleaned_data.get("tags", "")
            tag_names = [t.strip() for t in tags_str.split(",") if t.strip()]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                instance.tags.add(tag)
        return instance