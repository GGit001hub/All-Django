from django.shortcuts import render
from rest_framework import generics
from .models import Teacher,Student
from .serializers import PostSerializer, StudentSerializer
# Create your views here.


class TeacheCreateViewAPI(generics.ListAPIView):
    queryset = Teacher.objects.filter(status='active')
    serializer_class = PostSerializer

class StudentCreateViewAPI(generics.ListAPIView):
    queryset = Student.objects.filter(status='active')
    serializer_class = StudentSerializer
    
