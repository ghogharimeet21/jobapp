from django.contrib import admin
from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__","title","salary","date",)

    list_filter = ("date","salary","expiry",)

    search_fields = ("title","description",)
    search_help_text = "write in your query and hit enter"

    # fields = (("title","description"),"expiry",)
    exclude = ("title",)

# Register your models here.
admin.site.register(JobPost, JobAdmin)