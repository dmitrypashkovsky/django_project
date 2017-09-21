from django.contrib import admin
from .models import *


class DataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Data._meta.fields]
    search_fields = ["a", "b"]

    class Meta:
        model = Data


admin.site.register(Data, DataAdmin)