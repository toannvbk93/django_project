from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, DemoForm

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
            return redirect('/login/')
        return render(request, 'users/register.html', {'form': form})
class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile.html', context)
    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been update')
            return redirect('/profile/')
        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'users/profile.html', context)
    
class DemoView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = DemoForm()
        return render(request, 'users/demo.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = DemoForm(request.POST)
        if form.is_valid():
            return render(request, 'users/demo.html', {'form': form, 'your_name': request.POST.get('your_name')})

class ContactUsView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/contact.html')
