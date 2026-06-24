from django.urls import path
from .views import StudentAPIView, ProfileAPIView, HelloAPIView
from .views import SingleStudentAPIView

urlpatterns = [
    path('students/', StudentAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
    path('hello/', HelloAPIView.as_view()),
    path('student/<int:id>/', SingleStudentAPIView.as_view()),
    
]