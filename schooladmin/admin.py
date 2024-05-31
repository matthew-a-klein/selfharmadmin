from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(School, SchoolAdmin)