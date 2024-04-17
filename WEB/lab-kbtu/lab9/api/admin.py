from django.contrib import admin
from .models import Company, Vacancy

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address') 
    search_fields = ('name', 'city')  

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'company') 
    search_fields = ('name', 'company__name') 
    list_filter = ('company',)  
