from django.contrib import admin

from jobs.models import Category, Company, Country, Currency, JobOffer, Profile, Technology

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'created_at', 'updated_at')
    list_filter = ['updated_at', 'country']
    search_fields = ['user__name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'site_url', 'created_at', 'updated_at')
    list_filter = ['updated_at']
    search_fields = ['name', 'description', 'site_url']


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'seniority',
                    'english_level', 'category', 'country',
                    'seniority', 'english_level',
                    'salary_start', 'salary_end', 'currency',
                    'is_active', 'updated_at')
    list_filter = ['category', 'country',
                   'currency', 'is_active', 'updated_at']
    search_fields = ['position', 'company__name']


admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Currency)
admin.site.register(Technology)
