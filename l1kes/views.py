from l1kes.decorators import class_view_decorator
from django.contrib.auth.decorators import login_required
from mongotools.views import DetailView
from django.http import HttpResponseRedirect
from l1kes.models import Subscribe, Like


@class_view_decorator(login_required)
class LikeOrSubscribeView(DetailView):
    document = None
    action_type = None
    enable = True

    slug_field = 'pk'
    kwargs_slug_field = 'id'

    def get_object(self, queryset=None):
        queryset = queryset or self.document.objects
        return queryset.get(**{self.slug_field: \
            self.kwargs.get(self.kwargs_slug_field, None)})

    def get_redirect(self, request):
        return request.META.get('HTTP_REFERER', None) or '/'

    def get(self, request, *a, **kw):
        obj, _ = self.action_type.objects.get_or_create(\
            user=request.user, obj=self.get_object())
        obj.is_enabled = self.enable
        obj.save()
        return HttpResponseRedirect(self.get_redirect(request))


class LikeView(LikeOrSubscribeView):
    action_type = Like


class DislikeView(LikeOrSubscribeView):
    action_type = Like
    enable = False


class SubscribeView(LikeOrSubscribeView):
    action_type = Subscribe


class UnsubscribeView(LikeOrSubscribeView):
    action_type = Subscribe
    enable = False
