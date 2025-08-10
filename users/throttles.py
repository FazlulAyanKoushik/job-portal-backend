from rest_framework.throttling import ScopedRateThrottle

class LoginRateThrottle(ScopedRateThrottle):
    scope = "login"

class JobApplicationRateThrottle(ScopedRateThrottle):
    scope = "apply_job"
