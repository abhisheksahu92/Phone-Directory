from django.db import models
from django.urls import reverse

# Create your models here.
class PhoneModel(models.Model):
    gender_choice = (('Male','Male'),('Female','Female'))
    phone_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10,null=True,blank=True)
    last_name = models.CharField(max_length=10)
    phone = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(choices=gender_choice,max_length=6)

    def __str__(self):
        return self.first_name + '' if not self.middle_name else self.middle_name + self.last_name

    def get_absolute_url(self):
        return reverse('phone:phone-list')

class CallHistoryModel(models.Model):
    phone_id = models.ForeignKey(PhoneModel,related_name='phone_call_id',on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(null=True)

    def get_absolute_url(self):
        return reverse('phone:phone-list')