from dataclasses import field, fields
import imp
from importlib.metadata import files
from statistics import mode
from rest_framework import serializers
from .models import Movie, Rating

class MovieSearializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id', 'title', 'description')

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('id', 'stars', 'user', 'movie')

