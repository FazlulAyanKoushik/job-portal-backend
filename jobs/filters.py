import django_filters
from .models import JobPost

class JobPostFilter(django_filters.FilterSet):
    class Meta:
        model = JobPost
        fields = {
            'category': ['exact'],
            'location': ['exact'],
            'status': ['exact'],
        }
