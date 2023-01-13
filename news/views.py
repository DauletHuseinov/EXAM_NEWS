from django.shortcuts import render
from django_filters import filters

from .models import Comment, CommentStatus, NewsStatus, News
from .serializers import NewsSerializer, CommentSerializer
from .permissions import IsAuthorPermissions
from rest_framework import viewsets, generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class NewsAPIView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [ IsAuthorPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['updated', 'created']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class CommentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs.get('news_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author, news_id=self.kwargs.get('news_id'))



