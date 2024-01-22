from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from base.models import Book , Customer

# serializer for Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

@api_view(['GET'])
def index(req):
    return Response('hello')

# with serializer
@api_view(['GET','POST','DELETE','PUT'])
def home(req, id=-1):
    if req.method =='GET':
        if id > -1:
            temp_book=Book.objects.get(id=id)
            return Response (BookSerializer(temp_book,many=False).data)
        all_Books=BookSerializer(Book.objects.all(),many=True).data
        return Response (all_Books)
    if req.method =='POST':
        book_serializer = BookSerializer(data=req.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response ("post...")
    if req.method =='DELETE':
        temp_book=Book.objects.get(id=id)
        temp_book.delete()
        return Response ("del...")
    if req.method =='PUT':
        temp_book=Book.objects.get(id=id)
        ser = BookSerializer(data=req.data)
        old_book = Book.objects.get(id=id)
        res = ser.update(old_book, req.data)
        return Response(res)


@api_view(['GET'])
def about(req):
    return Response('about')

# without serializer
@api_view(['GET'])
def contact(req):
    res = []
    for x in Customer.objects.all():
        res.append({"name" : x.name , "age" : x.age})
    return Response(res)