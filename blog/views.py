from django.views import generic
from django.shortcuts import render

from .models import Blogger, BlogPost, Comment

# Create your views here.
def index(request):
    # Render the HTML template index.html
    return render(request, 'index.html')

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger
