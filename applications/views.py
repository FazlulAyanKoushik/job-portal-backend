from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters

from users.permissions import IsJobSeeker, IsEmployer
from users.throttles import JobApplicationRateThrottle
from .filters import ApplicationFilter
from .models import Application
from .serializers import ApplicationSerializer, ApplicationDetailSerializer
from .tasks import send_application_notification


class ApplyToJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsJobSeeker]
    throttle_classes = [JobApplicationRateThrottle]

    def perform_create(self, serializer):
        seeker = self.request.user
        job = serializer.validated_data['job']

        # Send notification email to employer (async)
        send_application_notification.delay(
            employer_email=job.employer.email,
            seeker_email=seeker.email,
            job_title=job.title,
        )

        serializer.save(seeker=seeker)


class EmployerApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ApplicationFilter
    ordering_fields = ['created_at']

    def get_queryset(self):
        return Application.objects.filter(
            job__employer=self.request.user
        ).select_related('job', 'seeker')
