from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

"""
urlpatterns = [
    path('', views.api_root),
    path('todos/', views.TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
"""

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls))
]