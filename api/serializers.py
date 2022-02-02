from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Movie, Rating

class UserSearializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password')
    extra_kwargs = {'password' : {'write_only': True, 'required': True}}

  def create(self, validated_data):
    user = User.objects.create(**validated_data)
    Token.objects.create(user=user)
    return user

class MovieSearializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('id', 'stars', 'user', 'movie')

