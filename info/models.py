from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

CATEGORY_CHOICES=(('single', 'single'),
                 ('double', 'double'), 
                 ('family', 'family'),
                 ('suite', 'suite')
                  
            

)
class Feature(models.Model):
    name = models.CharField(max_length=50, blank=False)
    def __str__(self) -> str:
        return f'{self.name}'


class Room(models.Model):
    room_no=models.IntegerField()
    name = models.CharField(max_length=50, blank=False)
    description=models.TextField(max_length=200, blank=False)
    feature=models.ManyToManyField(Feature)
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='single')
    free=models.BooleanField(default=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='img/', blank=True)

    def __str__(self) -> str:
        return f'{self.name} {self.category}'
    
    def get_price(self):
        return self.price
    
    def get_url(self):
        if self.image is not None: 
            return True    
        else:
            return False
    


