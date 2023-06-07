from social_network.models import UserActivity


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            try:
                activity = UserActivity.objects.get(user=request.user)
                activity.update_last_request()
            except UserActivity.DoesNotExist:
                UserActivity.objects.create(user=request.user)

        return response
