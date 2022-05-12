import json

from .models import Library
from .serializers import CursorSerializers
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


def list_all_book(request):
    """
    Function get all books
    """
    all_books = Library.get_all_books()
    serialize_data = CursorSerializers(all_books, many=True)

    return JsonResponse(serialize_data.data, safe=False)


@csrf_exempt
def create_book(request):
    """
        Function create a book in database if serliazer is valid
    """
    if request.method != 'POST':
        return JsonResponse({"message": "Method Not Valid, Please Send POST Request"})

    request_data = json.loads(request.body)

    book_id = request_data.get('id')
    cursor_serializer = CursorSerializers(data=request_data)

    if cursor_serializer.is_valid():
        cursor_serializer.save()

        return JsonResponse({"message": "Book Saved", "id": book_id}, status=status.HTTP_200_OK)

    return JsonResponse({"message": "Not Valid Book Datas"}, status=status.HTTP_406_NOT_ACCEPTABLE)


@csrf_exempt
def edit_book(request):
    """
    Function Edit Book Data
    """
    if request.method != 'POST':
        return JsonResponse({"message": "Method Not Valid, Please Send POST Request"})

    request_data = json.loads(request.body)

    book_id = request_data.get('id')
    book = Library.get_book_with_id(book_id=book_id)

    if book:
        reponse = Library.update_book_details(book_id=book_id, details=request_data)

        if reponse:
            return JsonResponse({'message': 'Book Data Updated'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Not Updated'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def delete_book(request, book_id):
    """
    Function delete book on database
    """
    result = Library.delete_book_with_id(book_id=book_id)

    if result:
        return JsonResponse({"message": "Book Deleted"}, status=status.HTTP_200_OK)

    return JsonResponse({"message": "Book Not Found"}, status=status.HTTP_404_NOT_FOUND)


def get_book(request, book_id):
    """
      Function return get book data
    """
    print(book_id, type(book_id))
    book = Library.get_book_with_id(book_id=book_id)

    return JsonResponse(book, status=status.HTTP_200_OK)
