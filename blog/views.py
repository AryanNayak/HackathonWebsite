from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
