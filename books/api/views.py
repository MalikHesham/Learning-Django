from rest_framework.response import Response
from rest_framework import status

from books.models import Book
from .serializers import BookSerializer,UserSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User has been registered successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def index(request):
    books = Book.objects.all()
    ser = BookSerializer(instance=books, many=True)
    return Response(data=ser.data,status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
@api_view(["POST",])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message" : "Book has been added successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success" : False,
        "errors" : serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(["PUT"])
def update(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message" : "Book has been updated successfully"
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def destroy(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return Response(data={
        "success": True,
        "message": "Book was deleted successfully"
    })