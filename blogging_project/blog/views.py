from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import BlogPost 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q  


# Blog List View (Shows Public Blogs + Author's Own Blogs)
class BlogListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        user = self.request.user
        return BlogPost.objects.filter(Q(visibility='public') | Q(author=user)).order_by('-created_at')

# Blog Detail View (Shows Individual Blog with Visibility Check)
class BlogDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'

    def get_queryset(self):
        user = self.request.user
        return BlogPost.objects.filter(Q(visibility='public') | Q(author=user))


# Blog Create View (Only for Logged-in Users)
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content', 'visibility']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Blog Update View (Only Author Can Edit)
class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'visibility']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user


# Blog Delete View (Only Author Can Delete)
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user

