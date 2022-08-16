from django.contrib import admin

# Register your models here.
from app.models import  App

class AppAdmin(admin.ModelAdmin):
    list_display = [field.name for field in App._meta.fields if field.name not in ('id')]


admin.site.register(App, AppAdmin)
