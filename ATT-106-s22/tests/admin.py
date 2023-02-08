from django.contrib import admin
from .models import Test
# Register your models here.


@admin.register(Test)
class TestRegister(admin.ModelAdmin):
    list_display = ['true_question','status','created_at']
    list_filter = ['status','created_at']
    search_fields = ['true_question',]
    list_editable = ['status',]
