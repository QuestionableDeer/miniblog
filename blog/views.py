from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Blogger, BlogPost, Comment
from blog.forms import CommentForm

# Create your views here.
def index(request):
    # Render the HTML template index.html
    return render(request, 'index.html')

@login_required
def post_comment(request, pk):
    '''View function for posting a comment to a specific blog'''
    blog_post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        # create form instance and populate it with data from request (binding)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment()
            comment.author = request.user
            comment.blog = blog_post
            comment.description = form.cleaned_data['description']

            comment.save()

            return HttpResponseRedirect(reverse('blog-post-detail', kwargs={'pk':pk}))
    else:
        form = CommentForm()

    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, 'blog/post_comment.html', context)

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger
