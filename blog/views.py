from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        context = {'posts': Post.objects.all()}
        return render(request, self.template_name, context)
class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    model = Post
    template_name = 'home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
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
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)