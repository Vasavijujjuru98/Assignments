from django.shortcuts import render
from .serializers import BookSerailizers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Book

# Create your views here.
class BookView(APIView):
    def post(self,request):
        serializer=BookSerailizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerailizers(books,many=True)
        return Response(serializer.data)
    
    def put(self,request,pk):
        book=Book.objects.get(pk=pk)
        serializer=BookSerailizers(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        book=Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)