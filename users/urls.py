from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from blog.views import AboutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register/', user_views.RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path ('about', AboutView.as_view(template_name='about.html'), name='about'),
    path('profile/', login_required(user_views.ProfileView.as_view()), name='profile'),
]