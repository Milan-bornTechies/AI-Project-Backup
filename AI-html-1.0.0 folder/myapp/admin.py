from django.contrib import admin
from .models import User,WorkSpace,Uploadfiles,Onboard,Admin_user,Pricing,Feedback,Training_Videos_Pricing
from .models import Post,Platform, YouTubeBlog, InstagramBlog,TikTokBlog, FacebookBlog, LinkedInBlog
from ckeditor.widgets import CKEditorWidget
from django import forms

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'author', 'published_date', 'enabled']  # Add enabled field here
    list_filter = ['enabled', 'published_date', 'author']  # Add enabled field to filter
    
class PlatformAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Platform
        fields = '__all__'

class PlatformAdmin(admin.ModelAdmin):
    form = PlatformAdminForm
    list_display = ['title', 'author', 'published_date', 'enabled']
    list_filter = ['enabled', 'published_date', 'author']
    
# Custom form for all blog models using CKEditor
class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        fields = '__all__'

# Admin class for all blog models
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ['title', 'author', 'published_date', 'enabled']
    list_filter = ['enabled', 'published_date', 'author']

admin.site.register(User)
admin.site.register(WorkSpace)
admin.site.register(Feedback)
admin.site.register(Uploadfiles)
admin.site.register(Onboard)
admin.site.register(Admin_user)
admin.site.register(Pricing)
admin.site.register(Training_Videos_Pricing)
admin.site.register(Post, PostAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(YouTubeBlog, BlogAdmin)
admin.site.register(InstagramBlog, BlogAdmin)
admin.site.register(TikTokBlog, BlogAdmin)
admin.site.register(FacebookBlog, BlogAdmin)
admin.site.register(LinkedInBlog, BlogAdmin)





