from django.urls import path
from .views import ApplyToJobView, EmployerApplicationListView

urlpatterns = [
    path('apply', ApplyToJobView.as_view(), name='apply-job'),
    path('employer-applications', EmployerApplicationListView.as_view(), name='employer-applications'),
]
