from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from django.http import HttpResponse

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
