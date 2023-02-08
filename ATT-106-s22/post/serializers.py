from rest_framework import serializers
from .models import Teacher, Student


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name','photo','subject','stars','status','created_add']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','photo','stars','status','created_add']

