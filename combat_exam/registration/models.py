from django.db import models

class User (models.Model):
    first_name = models.CharField(max_length= 30, blank=False)
    familly_name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=50)
    user_name = models.CharField(max_length=50, blank=False,unique=True)
    phone_number = models.CharField(max_length=22)
    location = models.CharField(max_length=60)
    password = models.CharField(max_length=30, blank=False)
    
    def __str__(self):
        return f'{self.user_name} : {self.phone_number} : {self.location}'


