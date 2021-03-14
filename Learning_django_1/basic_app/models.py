from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    roll = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name