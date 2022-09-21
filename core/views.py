from django.shortcuts import render
from core.models import Post
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.


class PostView(ListView):
    model = Post
    paginate_by: int = 2
    context_object_name = 'posts'
    template_name = 'home.html'
    ordering = ['title']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
