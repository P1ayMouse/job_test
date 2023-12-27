from django.contrib import admin

from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age')
    list_filter = ['name', 'surname', 'age']
