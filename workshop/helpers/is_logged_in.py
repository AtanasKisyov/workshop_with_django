from workshop.user_profile.models import Profile


def is_logged_in():
    user = Profile.objects.all()
    if len(user) > 0:
        return user[0]
    return False
