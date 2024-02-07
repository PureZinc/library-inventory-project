from django.urls import path
from . import views as v

# endpoint = 'library/{urlpath}'

urlpatterns = [
    path('books/', v.BookListView.as_view(), name='bookList'),  # getAPI
    path('books/<int:pk>/', v.BookView.as_view(), name='book'),  # getAPI
    path('addbook/', v.AddBookView.as_view(), name='createBook'),  # postAPI
    path('memberships/', v.UserMembershipView.as_view(), name='memberships'),  # getAPI
    path('booktrack/', v.BookTrackerView.as_view(), name='trackers'),  # getAPI
    path('mybooks/', v.MyBooksView.as_view(), name='myBooks'),  # getAPI
    path('rentbook/', v.RentBookView.as_view(), name='rentBook'),  # postAPI
    path('returnbook/<int:pk>/', v.ReturnBookView.as_view(), name='returnBook')  # deleteAPI
]
