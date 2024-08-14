from django.utils.deprecation import MiddlewareMixin

class SocialAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and not request.session.get('username'):
            request.session['username'] = request.user.username
            request.session['email'] = request.user.email if request.user.email else request.user.username
