from django.urls import path
from .views import JobPostCreateView, EmployerJobListView, JobPostDetailView, PublicJobListView

urlpatterns = [
    path('create', JobPostCreateView.as_view(), name='job-create'),
    path('my-jobs', EmployerJobListView.as_view(), name='employer-job-list'),
    path('<int:pk>', JobPostDetailView.as_view(), name='job-detail'),
    path('public', PublicJobListView.as_view(), name='public-job-list'),
]
