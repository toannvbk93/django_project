from django.contrib import admin
from django.urls import path
from blog.views import ( 
    HomeView,
    AboutView,
    PostListView,
    PostDetailsView,
    PostCreateView,
    PostUpdateView
    )


app_name="blog"
urlpatterns = [
    # path('', HomeView.as_view(), name="home"),
    # path('about/', AboutView.as_view(), name="about")
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailsView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
]
