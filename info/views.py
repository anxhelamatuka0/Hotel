from django.shortcuts import render
from .models import Room

# Create your views here.


def home(request):
    return render(request,'info/home.html')

def about(request):
    return render(request,'info/about.html')

def contact(request):
    return render(request,'info/contact.html')

def rooms(request):
    single=Room.objects.filter(category='single')
    double=Room.objects.filter(category='double')
    family=Room.objects.filter(category='family')
    suite=Room.objects.filter(category='suite')
    context={'single':single, 'double':double, 'family':family, 'suite':suite}
    print(single)
    return render(request,'info/rooms.html', context)
