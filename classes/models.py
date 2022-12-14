from django.db import models
from django.db.models.signals import pre_save

from datetime import datetime,date
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
#User database to store the students in the Yoga Classes.
def calculate_age(bday,d=None):
    bday = str(bday)
    bday = datetime.strptime(bday, '%Y-%m-%d')
    if d is None:
        d = date.today()
    temp= int(d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))
    # print(temp)
    if temp<=0:
        return 0
    else:
        return temp

class User(AbstractUser):
    username=models.CharField(max_length=255,primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0)
    dob = models.DateField()
    phone = models.CharField(max_length=20)
    def save(self, *args, **kwargs):
        self.age = calculate_age(self.dob)
        self.username = self.email
        super().save(*args, **kwargs)
    



# Signal to automatically save age based on DOB
   



class EnrolledBatches(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    batch = models.CharField(max_length=50)
    month = models.DateField() #month and year they are enrolled for.
    payment_status = models.BooleanField(default=True) #currently set to true due to no backend of payment.

 
