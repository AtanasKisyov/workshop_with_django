from django import template

from workshop.user_profile.models import Profile

register = template.Library()


@register.simple_tag()
def logged_user():
    return Profile.objects.count() > 0
