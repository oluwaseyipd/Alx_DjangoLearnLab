from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image



# User Profile
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Extra fields
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.jpg')
    banner_image = models.ImageField(upload_to='banner_pictures', default='banner_pictures/default.jpeg')

    # Track creation time
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    def save(self):
        super().save()

        # Resize profile image
        img = Image.open(self.profile_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

# Tag 
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Blog Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")


    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# Blog Comments
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})


