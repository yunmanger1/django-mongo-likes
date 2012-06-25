from django import template
register = template.Library()

from l1kes.models import Like, Subscribe


def user_action(document=Like):
    def like_or_subscribe(user, obj):
        """
        Template usage: {% if request.user|likes:obj %}
        """
        if not user.is_authenticated():
            return False
        return document.objects.filter(\
            obj=obj, is_enabled=True, user=user).count()

    return like_or_subscribe


def action_count(document=Like):
    def like_or_subscribe_count(obj):
        return document.objects.filter(is_enabled=True, obj=obj).count()
    return like_or_subscribe_count

register.filter('likes', user_action(Like))
register.filter('subscribed', user_action(Subscribe))
register.filter('like_count', action_count(Like))
register.filter('subscribe_count', action_count(Subscribe))
