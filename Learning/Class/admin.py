from django.contrib import admin
from .models import Contact, Newsletter

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    list_filter = ['name', 'email', 'date_time', 'subject']
    search_fields = ['name', 'email', 'subject']

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_time']
    list_filter = ['date_time']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)