from rest_framework import generics, permissions
from .serializers import BookSer, BookTrackerSer, UserMembershipSer
from .models import Book, BookTracker, UserMembership
from rest_framework.response import Response
from django.http import Http404
from django.db.models import F


class UserMembershipView(generics.ListAPIView):
    serializer_class = UserMembershipSer
    queryset = UserMembership.objects.all()


class BookListView(generics.ListAPIView):
    serializer_class = BookSer
    queryset = Book.objects.all()


class AddBookView(generics.CreateAPIView):
    serializer_class = BookSer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        membership = UserMembership.objects.get(user=user)

        if membership.is_librarian:
            serializer.save()
            return Response({"message": "Book added to library"}, status=200)
        
        elif membership.is_member:
            return Response({"message": "Only librarians can add books!"}, status=400)
        
        return Response({"message": "User membership not found!"}, status=400)


class BookTrackerView(generics.ListAPIView):
    serializer_class = BookTrackerSer
    queryset = BookTracker.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class MyBooksView(generics.ListAPIView):
    serializer_class = BookTrackerSer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        return BookTracker.objects.filter(user=user)


class BookView(generics.RetrieveAPIView):
    serializer_class = BookSer
    queryset = Book.objects.all()
    lookup_field = 'pk'
        

class RentBookView(generics.CreateAPIView):
    serializer_class = BookTrackerSer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = self.request.user.id
            membership = UserMembership.objects.get(user=user)
            if membership.is_member:
                try:

                    book = Book.objects.get(id=serializer.validated_data["book"].id)
                    if book.stock > 0:
                        Book.objects.filter(id=book.id).update(stock=F("stock") - 1)

                        BookTracker.objects.create(user=membership, book=book)
                        return Response({"message": "Successfully rented book"}, status=200)
                    
                except Book.DoesNotExist:
                    raise Http404("Book does not exist")
                
                return Response({"message": "Book is out of stock"}, status=400)
            return Response({"message": "Only members can rent books!"}, status=400)
        else:
            Response(serializer.errors, status=400)


class ReturnBookView(generics.DestroyAPIView):
    queryset = BookTracker.objects.all()
    serializer_class = BookTrackerSer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            book = instance.book

            book.stock += 1
            book.save()

            instance.delete()
            return Response({"message": "Instance deleted successfully"}, status=204)
        except Exception as e:
            print(e)
            return Response({"message": f"{e}"}, status=400)
