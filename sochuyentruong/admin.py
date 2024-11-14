from django.contrib import admin
from .models import NamHoc
# Register your models here.


@admin.register(NamHoc)
class NamHocAdmin(admin.ModelAdmin):
    list_display = ("id", "tennamhoc")
    list_filter = ['tennamhoc']
    search_fields =['tennamhoc__contains']

