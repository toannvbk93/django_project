from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        context = {'posts': Post.objects.all()}
        return render(request, self.template_name, context)
class AboutView(TemplateView):
    template_name = "about.html"
