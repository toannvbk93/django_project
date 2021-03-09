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
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complate/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complate.html'),
        name='password_reset_complate'),
    path('demo/', user_views.DemoView.as_view(), name='demo'),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='users/change_password.html', success_url='login/'), name='change-password')
]