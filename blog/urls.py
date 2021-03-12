from django.contrib import admin
from django.urls import path
from blog.views import ( 
    HomeView,
    AboutView,
    PostListView,
    PostDetailsView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SearchView
)


app_name="blog"
urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailsView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('searchresult/', SearchView.as_view(), name="search-post")
]
