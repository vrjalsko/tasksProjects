from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', include([
        path('', views.UserListCreateAPIView.as_view(), name='user-list'),
        path('<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    ])),

    path('tasks/', include([
        path('', views.TaskListCreateAPIView.as_view(), name='task-list'),
        path('<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    ])),

    path('projects/', include([
        path('', views.ProjectListCreateAPIView.as_view(), name='project-list'),
        path('<int:pk>/', views.ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
    ])),

    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('login/', views.CustomObtainAuthToken.as_view(), name='login'),
]
