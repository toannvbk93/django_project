from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import SearchForm
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    form = SearchForm
    def get(self, request, *args, **kwargs):
        context = {'posts': Post.objects.all()}
        return render(request, self.template_name, context)
    

class SearchView(ListView):
    template_name="search_result.html"
    model = Post
    context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['search_content'] = self.request.GET['search']
        return data
    def get_queryset(self):
        search_content = self.request.GET['search']
        posts = Post.objects.filter(title__icontains=search_content).order_by('-date_posted')
        if not posts:
            return Post.objects.all()
        else:
            return posts
            

class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    model = Post
    template_name = 'home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 10

class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False