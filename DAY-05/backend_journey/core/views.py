from django.shortcuts import render

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