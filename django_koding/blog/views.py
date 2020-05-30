from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from blog.models import Post


class PostFeed(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['posts'] = Post.objects.all().order_by('date')
        return context
