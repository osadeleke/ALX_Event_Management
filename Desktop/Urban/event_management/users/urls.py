# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet
# # from .views import UserListCreateView, UserDetailView

# router = DefaultRouter()
# router.register(r'users', UserViewSet)


# urlpatterns = router.urls

from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]