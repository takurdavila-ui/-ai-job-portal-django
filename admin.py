from django.contrib import admin
from .models import Company, Job, Application, Profile


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'user')
    search_fields = ('name', 'location')
    list_filter = ('location',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('location', 'created_at')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('user__username', 'job__title')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'skills')