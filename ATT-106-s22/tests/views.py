from django.shortcuts import render
from rest_framework import generics
from .serializers import TestSerializer
from .models import Test

# Create your views here.


class QuestionsViewAPI(generics.ListAPIView):
    queryset = Test.objects.filter(status='active')
    serializer_class = TestSerializer

