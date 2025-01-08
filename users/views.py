# from rest_framework import viewsets, permissions, generics
# from .models import CustomUser
# from .serializers import UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_permissions(self):
#         if self.action in ['create', 'list']:
#             return [permissions.AllowAny()]  # Anyone can register or view the user list
#         return super().get_permissions()

#     def perform_create(self, serializer):
#         # Automatically set the password properly using `set_password`
#         user = serializer.save()
#         user.set_password(user.password)
#         user.save()

from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny


class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer