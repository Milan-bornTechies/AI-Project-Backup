from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    pswd = models.CharField(max_length=20)
    def __str__(self):
        return self.email 

class Onboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace_username = models.CharField(max_length=50)
    workspace_name = models.CharField(max_length=50)

    def __str__(self):
        return self.workspace_username

class WorkSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    gender = models.TextField(max_length=500)
    generated_text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField(blank=True, null=True) 
    edited_video_url = models.URLField(blank=True, null=True) 
    def __str__(self):
        return self.message+" - "+self.user.name
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.email}" 
       
class Pricing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_session_id = models.CharField(max_length=500, blank=True, null=True)
    price_of_plan = models.IntegerField(blank=True, null=True)
    date_of_created = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.user.name
        
class Training_Videos_Pricing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_session_id = models.CharField(max_length=500, blank=True, null=True)
    price_of_plan = models.IntegerField(blank=True, null=True)
    plan_name = models.TextField(max_length=500, default="Free")
    date_of_created = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.user.name        
           
class Uploadfiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    segment_url_1 = models.URLField(blank=True, null=True)
    segment_url_2 = models.URLField(blank=True, null=True)
    segment_url_3 = models.URLField(blank=True, null=True)
    segment_url_4 = models.URLField(blank=True, null=True)
    segment_url_5 = models.URLField(blank=True, null=True)
    segment_url_6 = models.URLField(blank=True, null=True)
    segment_url_7 = models.URLField(blank=True, null=True)
    segment_url_8 = models.URLField(blank=True, null=True)
    segment_url_9 = models.URLField(blank=True, null=True)
    segment_text_1 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_2 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_3 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_4 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_5 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_6 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_7 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_8 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_9 = models.TextField(max_length=500, blank=True, null=True)
    upload_video_1 = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_video_2 = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_video_3 = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_video_4 = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_video_5 = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_video_6 = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_video_7 = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_video_8 = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_video_9 = models.FileField(upload_to='videos/', blank=True, null=True)
    edited_video = models.FileField(upload_to='videos/', blank=True, null=True)
    def __str__(self):
        return self.workspace.message+" - "+self.user.name

class Admin_user(models.Model):
    email = models.EmailField()
    pswd = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    enabled = models.BooleanField(default=True)  # Add this line

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Platform(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='platform_images/', blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class YouTubeBlog(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='youtube_blog_images/', blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class InstagramBlog(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='instagram_blog_images/', blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class TikTokBlog(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='tiktok_blog_images/', blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class FacebookBlog(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='facebook_blog_images/', blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class LinkedInBlog(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='linkedin_blog_images/', blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    

    