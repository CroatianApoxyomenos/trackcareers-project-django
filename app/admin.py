from django.contrib import admin

from app.models import JobPost, Location, Author, Skills


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Basic information', {
            'fields': ('title', 'description')
        }),
        ('More information', {
            'fields': ('expiry', 'salary', 'slug')
        })
    )


admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
