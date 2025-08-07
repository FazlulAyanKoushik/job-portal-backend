from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters

from users.permissions import IsEmployer
from .filters import JobPostFilter
from .models import JobPost
from .serializers import JobPostSerializer


class JobPostCreateView(generics.CreateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsEmployer]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

class EmployerJobListView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsEmployer]

    def get_queryset(self):
        return JobPost.objects.filter(employer=self.request.user)

class JobPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsEmployer]

    def get_queryset(self):
        return JobPost.objects.filter(employer=self.request.user)


class PublicJobListView(generics.ListAPIView):
    queryset = JobPost.objects.filter(status='OPEN')
    serializer_class = JobPostSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = JobPostFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

