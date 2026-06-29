from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from django.http import HttpResponse

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


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


class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    
class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser
            
        })
    
class SingleStudentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        except Student.DoesNotExist:
            return Response({"error": "Student not found"})
        
class CreateStudentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):   
     return Response(
    {"message": "Student created successfully"},
    status=status.HTTP_201_CREATED
)
    
@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
def update_student(request,id):

    try:
        student = Student.objects.get(id=id)

    except Student.DoesNotExist:

        return Response(
            {"error":"Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    

    serializer = StudentSerializer(
        student,
        data=request.data,
        partial=(request.method=='PATCH')
    )


    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)


    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_student(request, id):

    try:
        student = Student.objects.get(id=id)

    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    student.delete()

    return Response(
        {"message": "Student deleted successfully"},
        status=status.HTTP_200_OK
    )

    