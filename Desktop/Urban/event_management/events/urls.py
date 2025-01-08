from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, AttendeeViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'attendees', AttendeeViewSet, basename='attendee')
router.register(r'comments', CommentViewSet)



urlpatterns = [
    path('', include(router.urls)), 
]