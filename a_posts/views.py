from django.shortcuts import render
from .models import *

# Create your views here.
def home_view(request):
  posts = Post.objects.all()
  context = {
    'page' : 'Home',
    'posts' : posts,
  }
  if request.htmx:
    return render(request, 'a_posts/partials/_home.html', context)
  return render(request, 'a_posts/home.html', context)

def explore_view(request):
  context = {
    'page' : 'Explore',
    'partial' : request.htmx,
  }
  if request.htmx:
    return render(request, 'a_posts/partials/_explore.html', context)
  return render(request, 'a_posts/explore.html', context)

def upload_view(request):
  context = {
    'page' :'Upload',
    'partial' : request.htmx,
  }
  if request.htmx:
    return render(request, 'a_posts/partials/_upload.html', context)
  return render(request, 'a_posts/upload.html', context)