from django.contrib import admin
from django.urls import path
from blog.views import HomeView, AboutView, PostListView, PostDetailsView, PostCreateView


app_name="blog"
urlpatterns = [
    # path('', HomeView.as_view(), name="home"),
    # path('about/', AboutView.as_view(), name="about")
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailsView.as_view(), name="detail"),
    path('post/new/', PostCreateView.as_view(), name="create"),
]
