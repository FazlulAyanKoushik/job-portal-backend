from django.contrib import admin
from .models import Application
from users.models import User

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'job', 'applied_at')
    list_filter = ('applied_at', 'job')
    search_fields = ('seeker__email', 'job__title')
    ordering = ('-applied_at',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "seeker":
            kwargs["queryset"] = User.objects.filter(role="SEEKER")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Application, ApplicationAdmin)