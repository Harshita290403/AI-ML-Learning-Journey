from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
def about(request):
    return HttpResponse("This is the About Page.")

def contact(request):
    return HttpResponse("Contact us at: hello@example.com")

def profile(request):
    context = {
        'name': 'Harshita',
        'college': 'BABU BANARASI DAS',
        'year': '3rd Year',
        'skills': 'Python, Django, APIs'
    }

    return render(request, 'profile.html', context)

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django REST Framework!"})

from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class ProfileAPIView(APIView):
    def get(self, request):
        return Response({
            "name": "Harshita",
            "domain": "Backend Development",
            "goal": "Become proficient in Django and APIs"
        })
    
class SingleStudentAPIView(APIView):
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        except Student.DoesNotExist:
            return Response({"error": "Student not found"})