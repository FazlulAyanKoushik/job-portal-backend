from django.db import models
from users.models import User
from jobs.models import JobPost

class Application(models.Model):
    seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('seeker', 'job')  # prevent multiple applications

    def __str__(self):
        return f"{self.seeker.email} applied to {self.job.title}"
