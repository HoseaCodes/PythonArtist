from django.shortcuts import render

# Create your views here.

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request,'home.html')