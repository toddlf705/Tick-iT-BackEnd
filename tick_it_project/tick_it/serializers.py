from rest_framework import serializers
from .models import Venue, Event

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'image', 'address', 'policies', 'city', 'capacity', 'description', 'parking')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.PrimaryKeyRelatedField(queryset=Venue.objects.all())

    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'time', 'image','description', 'venue', 'price')