from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

class RegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! you are now able to login')
            return redirect('login/')
        return render(request, 'users/register.html', {'form': form})
class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/profile.html')