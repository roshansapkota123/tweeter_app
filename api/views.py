from django.shortcuts import render
from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetSerializer

# Create your views here.

class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
