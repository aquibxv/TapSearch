from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PDF


# Register your models here.
class PDFAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

admin.site.register(PDF, PDFAdmin)