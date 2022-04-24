from django.db import models

class Contact(models.Model):
    name =models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=200, blank=True)
    message=models.TextField()
   

    def __str__(self):
        return self.name