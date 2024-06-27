from django.contrib import admin
from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__","title","salary","date",)

    list_filter = ("date","salary","expiry",)

# Register your models here.
admin.site.register(JobPost, JobAdmin)