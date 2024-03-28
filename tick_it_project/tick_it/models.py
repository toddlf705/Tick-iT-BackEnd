from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()  
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100, default = 'No city')
    capacity = models.IntegerField(default=1)
    description = models.TextField(default = 'No description')
    parking = models.TextField(default = 'No parking')
    policies = models.TextField(default = 'No policies')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    image = models.URLField(default = 'www.fake.com')  
    description = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    price = models.CharField(max_length=50, default = 'free')

    def __str__(self):
        return self.name

