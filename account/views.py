from django.shortcuts import render
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorSerializer
from rest_framework import viewsets, status


# Create your views here.


class AuthorRegisterAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def create_author(self, request, pk=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save(
                author=pk
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
