from django.shortcuts import redirect
from social_core.pipeline.partial import partial
from .models import User

@partial
def custom_redirect(backend, user, response, *args, **kwargs):
    user_social_auth = user.social_auth.filter(provider=backend.name).first()

    if user_social_auth and user_social_auth.extra_data:
        social_data = user_social_auth.extra_data
        email = social_data.get('email', user.username)

        # Save or update the user details in your custom User model
        user_instance, created = User.objects.get_or_create(email=email, defaults={'name': user.username})

        # Set session data for the user
        kwargs['request'].session['username'] = user_instance.name
        kwargs['request'].session['email'] = email

        if created:
            # User is logging in for the first time
            return redirect('onboard', pk=user_instance.pk)
        else:
            # User has logged in before
            return redirect('work_space', pk=user_instance.pk)

    return None  # Continue with default redirect behavior if not handled
