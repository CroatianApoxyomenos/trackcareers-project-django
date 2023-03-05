from django.contrib import admin

from app.models import JobPost


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Basic information', {
            'fields' : ('title', 'description')
        }),
        ('More information', {
            'fields': ('expiry', 'salary', 'slug')
        })
    )


admin.site.register(JobPost, JobAdmin)
