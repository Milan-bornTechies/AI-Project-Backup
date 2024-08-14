from django.db.models.signals import post_save
from django.dispatch import receiver
from social_django.models import UserSocialAuth
from .models import User

# @receiver(post_save, sender=UserSocialAuth)
# def save_social_user_info(sender, instance, created, **kwargs):
    # if created:
    #     user = instance.user
    #     social_data = instance.extra_data
    #     username = user.username
        
    #     if 'email' in social_data:
    #         email = social_data['email']
    #     else:
    #         email = username

    #     # Create or update user in custom User table
    #     User.objects.update_or_create(
    #         email=email,
    #         defaults={
    #             'name': username,
    #         }
    #     )
