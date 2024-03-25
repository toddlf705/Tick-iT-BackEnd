from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()  
    address = models.CharField(max_length=200)
    policies = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(format='%I:%M %p')
    image = models.URLField()  
    address = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

