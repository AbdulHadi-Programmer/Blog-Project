from django.shortcuts import render, get_object_or_404, redirect
from .models import * 
from .forms import PostForm, ProfileForm 
# ------------------------------------------------------------------------------------------ 
# Page	         -|-   URL	                 -|-  * Description  *                         |
# ------------------------------------------------------------------------------------------ 
# Homepage	     -|-    /	                 -|-   Shows latest blog posts                 |
# Post Detail	 -|-   /post/<id>/	         -|-   Displays a single post with comments    |
# Create Post	 -|-   /create/	             -|-   Form for creating a new post            |
# Author Profile -|-   /author/<username>/	 -|-   Displays an author's profile and posts  |
# Tagged Posts	 -|-   /tag/<tagname>/	     -|-   Shows all posts with a specific tag     |
# ------------------------------------------------------------------------------------------ 

# Home Page :
def home_page(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

# Post Create Edit and View Detail :
# def post_detail(request):
#     return render(request, 'post_detail.html')
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.views = F('views') + 1  # Increase views count
    post.save(update_fields=['views'])

    comments = post.comments.filter(is_approved=True)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


def post_form(request, id=None):
    if id:
        post = get_object_or_404(Post, id=id)
    else:
        post = None 

    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm(instance = post)
    return render(request, 'post_form.html', {'form': form, 'post': post})


def author_profile(request):
    return render(request, 'author_profile.html')


def tagged_post(request):
    return render(request, 'tagged_post.html')

def tagged_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = tag.posts.all()
    return render(request, 'tagged_posts.html', {'tag': tag, 'posts': posts})
