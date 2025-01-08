from rest_framework import serializers
from .models import Event, Attendee, Comment
from django.utils import timezone
from users.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Event
        fields = '__all__'

    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Event date and time cannot be in the past.")
        return value

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['event', 'user', 'status', 'registered_at']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'event', 'user', 'text', 'created_at']
