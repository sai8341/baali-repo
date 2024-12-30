from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'company', 'location', 'posted_by', 'posted')
    list_filter = ('category', 'posted_by')  
    search_fields = ('title', 'company', 'location')

    def save_model(self, request, obj, form, change):
        if not obj.posted_by:  
            obj.posted_by = request.user
        super().save_model(request, obj, form, change)
