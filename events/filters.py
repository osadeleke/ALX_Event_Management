import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    location = django_filters.CharFilter(lookup_expr='icontains', label='Location')
    start_date = django_filters.DateTimeFilter(field_name='date_time', lookup_expr='gte', label='Start Date')
    end_date = django_filters.DateTimeFilter(field_name='date_time', lookup_expr='lte', label='End Date')

    class Meta:
        model = Event
        fields = ['title', 'location', 'start_date', 'end_date']
