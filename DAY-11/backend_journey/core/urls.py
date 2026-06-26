from django.urls import path
from .views import StudentAPIView, ProfileAPIView, HelloAPIView
from .views import SingleStudentAPIView
from .views import CreateStudentAPIView
from .views import update_student, delete_student
from .views import StudentListCreateView
from .views import StudentDetailView

urlpatterns = [
    
    path('profile/', ProfileAPIView.as_view()),
    path('hello/', HelloAPIView.as_view()),
    path('student/<int:id>/', SingleStudentAPIView.as_view()),
    path('student/update/<int:id>/', update_student),
    path('student/delete/<int:id>/', delete_student),
    path('students/', StudentListCreateView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
]


