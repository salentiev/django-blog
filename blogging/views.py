from django.shortcuts import render
from django.http import Http404
from blogging.models import Post
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'
