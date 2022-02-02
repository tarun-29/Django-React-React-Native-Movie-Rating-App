from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from api.models import Movie, Rating
from django.contrib.auth.models import User
from api.serializers import MovieSearializer, RatingSerializer, UserSearializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSearializer

class MovieViewSet(ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSearializer
  authentication_classes = (TokenAuthentication, )
  permission_classes = (IsAuthenticated)

  @action(detail=True, methods=['POST'])
  def rate_movie(self, request, pk=None):

    if 'stars' in request.data:
      movie = Movie.objects.get(id=pk)
      stars = request.data['stars']
      user = request.user

      try: 
        rating = Rating.objects.get(user=user.id, movie=movie.id)
        rating.stars = stars
        rating.save()
        serializer = RatingSerializer(rating, many=False)
        response = {'message': "Rating Updated", 'result' : serializer.data}
        return Response(response, status=status.HTTP_200_OK)

      except:
        Rating.objects.create(user=user, movie=movie, stars=stars)
        rating.save()
        serializer = RatingSerializer(rating, many=False)
        response = {'message': "Rating Created", 'result' : serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    else : 
      response = {'message': "You need to provide stars"}
      return Response(response, status=status.HTTP_400_BAD_REQUEST)

    
class RatingViewSet(ModelViewSet):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer
  authentication_classes = (TokenAuthentication, )
  permission_classes = (IsAuthenticated)

  def update(self, request, *args, **kwargs):
    response = {'message': "You can't update rating like that"}
    return Response(response, status=status.HTTP_400_BAD_REQUEST)

  def create(self, request, *args, **kwargs):
    response = {'message': "You can't create rating like that"}
    return Response(response, status=status.HTTP_400_BAD_REQUEST)
