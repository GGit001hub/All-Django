from django.contrib import admin
from .models import Teacher,Student
# Register your models here.

@admin.register(Teacher)
class RegisterPost(admin.ModelAdmin):
    list_display = ('name','subject','stars','status','created_add')
    list_filter = ('subject','stars','created_add','status')
    search_fields = ('subject',)
    sorted_by = ('-created_add',)


@admin.register(Student)
class RegisterPost(admin.ModelAdmin):
    list_display = ('name','status','stars','created_add')
    list_filter = ('created_add','stars','status')
    search_fields = ('subject',)