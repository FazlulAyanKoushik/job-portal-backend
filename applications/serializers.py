from rest_framework import serializers

from jobs.serializers import JobPostSerializer
from users.serializers import UserSerializer
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'job', 'resume', 'applied_at']
        read_only_fields = ['seeker', 'applied_at']



class ApplicationDetailSerializer(serializers.ModelSerializer):
    seeker = UserSerializer(read_only=True)
    job = JobPostSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'job', 'seeker', 'applied_at']
