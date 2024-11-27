from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    colorCode = models.CharField(max_length=7, default='#FFFFFF')  
    textColorCode = models.CharField(max_length=7, default='#000000')  

    def __str__(self):
        return self.name

    
