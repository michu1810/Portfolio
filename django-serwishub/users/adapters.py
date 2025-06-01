from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class NoSignupAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return True

    def populate_user(self, request, sociallogin, data):

        user = super().populate_user(request, sociallogin, data)
        user.email = data.get('email')
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')
        return user