from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = "blog"
urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('about/', views.AboutView.as_view(), name="about"),
    path('post/<pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('post/new/', views.CreatePostView.as_view(), name="post_new"),
    path("post/<pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path('post/<pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name="post_draft_list"),
    path('post/<pk>/comments/', views.add_comment_to_post, name="add_comment_to_post"),
    path('comment/<pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/delete', views.comment_removed, name='comment_removed'),
    path("post/<pk>/public", views.post_public, name="post_publish")
]