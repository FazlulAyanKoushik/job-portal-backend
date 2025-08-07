from rest_framework import generics, permissions
from .models import Application
from .serializers import ApplicationSerializer
from users.permissions import IsJobSeeker
from jobs.models import JobPost
from .tasks import send_application_notification

class ApplyToJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsJobSeeker]

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
