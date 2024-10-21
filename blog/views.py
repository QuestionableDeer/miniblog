from django.views import generic
from django.shortcuts import render

from .models import Blogger, BlogPost, Comment

# Create your views here.
def index(request):
    # Render the HTML template index.html
    return render(request, 'index.html')

class BlogPostListView(generic.ListView):
    model = BlogPost

class BlogPostDetailView(generic.DetailView):
    model = BlogPost
