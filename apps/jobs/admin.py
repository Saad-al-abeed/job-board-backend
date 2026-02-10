from django.contrib import admin
from .models import JobCategory, Job

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'category', 'location', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
