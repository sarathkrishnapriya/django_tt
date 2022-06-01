from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    # numberz = {
    #     'name' : ['Arjun','Vishnu','Sarath'],
    # }

    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

   

