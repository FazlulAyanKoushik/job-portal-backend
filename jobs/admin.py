from django.contrib import admin
from .models import JobPost
from users.models import User

class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'category', 'status', 'created_at')
    list_filter = ('status', 'category', 'location', 'created_at')
    search_fields = ('title', 'description', 'location', 'category', 'employer__username')
    ordering = ('-created_at',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employer":
            kwargs["queryset"] = User.objects.filter(role="EMPLOYER")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(JobPost, JobPostAdmin)