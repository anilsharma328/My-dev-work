from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    phone_number=models.IntegerField()

"""
    def __str__(self):
        return self.name
"""