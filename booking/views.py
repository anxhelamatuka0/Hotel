from django.shortcuts import render,get_object_or_404, redirect
from info.models import Room
from .forms import BookingForm
from django.http import HttpResponse


# Create your views here.


def room(request, pk):
    room=get_object_or_404(Room, pk=pk)
    form=BookingForm()
    request.session['room']=pk
    return render(request, 'booking/room.html', {'room':room, 'form':form})


def booking(request):
    
    form=BookingForm()
    room_pk=''
    if 'room' in request.session:
        room_pk=request.session['room']
    print('Room pk',room_pk)
    room=get_object_or_404(Room,pk=room_pk)
    print('Room pk',room)

    if request.method == 'POST':
        print('if metod')
        form=BookingForm(request.POST)
        if form.is_valid():
            print('if form')
            record=form.save(commit=False)
            if record.checkout > record.checkin:
                print('if check date')
                record.room=room
                record.save()
                print('Record', record)
                room.free=False
                room.save()
                return HttpResponse('success')
        else:
            return HttpResponse('Error')
    del request.session['room']
    return HttpResponse('success')

