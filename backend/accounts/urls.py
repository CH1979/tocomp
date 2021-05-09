from django.urls import path
from . import views


urlpatterns = [
    path(
        'profile/',
        views.ProfileView.as_view(),
        name='profile-detail'
    ),
    path(
        'groups/create/',
        views.GroupCreateView.as_view(),
        name='group-create'
    ),
    path(
        'courses/create/',
        views.CourseCreateView.as_view(),
        name='course-create'
    ),
    path(
        'courses/<int:pk>/update/',
        views.CourseUpdateView.as_view(),
        name='course-update'
    ),
    path(
        'courses/<int:pk>/update/',
        views.CourseDeleteView.as_view(),
        name='course-delete'
    )
]
