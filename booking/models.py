from django.db import models
from django.core.validators import RegexValidator
from info.models import Room
from datetime import datetime

# Create your models here.

class Booking(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    email=models.EmailField()
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}',message='the phone no must be entered in the format +000 up to 15 digits')
    phone=models.CharField(validators=[phone_regex], max_length=17,blank=True)
    room=models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    checkin=models.DateField(default=datetime.now)
    checkout=models.DateField(blank=False)
    price=models.DecimalField(max_digits=6, decimal_places=2)


    def save(self, *args, **kwargs):
        days=self.checkout-self.checkin
        self.price=self.room.get_price()*days.days
        super(Booking, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.email}' 
    