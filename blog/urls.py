from django.contrib import admin
from django.urls import path
from blog.views import HomeView, AboutView


app_name="blog"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # path('about/', AboutView.as_view(), name="about")
]
