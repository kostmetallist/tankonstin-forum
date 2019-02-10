from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .           import views
from .views      import (
    TopicDetailView, 
    MessageCreateView, 
    SectionListView, 
    MessageDeleteView,
    ForumUserDetailView,
    SearchListView
)

urlpatterns = [
    path("", views.forumHome, name="forum-home"),
    path("index/", SectionListView.as_view(), name="forum-index"),
    path("register/", views.userRegistration, name="user-registration"),
    path("login/", LoginView.as_view(template_name="forum/user-login.html"), name="user-login"),
    path("logout/", LogoutView.as_view(template_name="forum/index.html"), name="user-logout"),
    path("search/", SearchListView.as_view(), name="forum-search-results"),
    path("user/<int:pk>/", ForumUserDetailView.as_view(), name="user-detail"),
    path("user/edit/<int:userid>/", views.userProfileEditing, name="user-edit"),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path("message/create/topic/<int:topic>/", MessageCreateView.as_view(), name="message-create"),
    path("message/delete/<int:pk>/", MessageDeleteView.as_view(), name="message-delete"),
]