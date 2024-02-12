from django.urls import path
from . import views as v
from . import views_auth as auth

# endpoint = 'library/{urlpath}'

urlpatterns = [
    path('books/', v.BookListView.as_view(), name='bookList'),  # listAPI
    path('books/<int:pk>/', v.BookView.as_view(), name='book'),  # getAPI
    path('addbook/', v.AddBookView.as_view(), name='createBook'),  # postAPI
    path('memberships/', v.UserMembershipView.as_view(), name='memberships'),  # listAPI
    path('booktrack/', v.BookTrackerView.as_view(), name='trackers'),  # getAPI
    path('mybooks/', v.MyBooksView.as_view(), name='myBooks'),  # listAPI
    path('rentbook/', v.RentBookView.as_view(), name='rentBook'),  # postAPI
    path('returnbook/<int:pk>/', v.ReturnBookView.as_view(), name='returnBook'),  # deleteAPI

    path('auth/register/', auth.RegisterView.as_view(), name='register'),
    path('auth/login/', auth.LoginView.as_view(), name='login'),
    path('auth/logout/', auth.LogoutView.as_view(), name='logout'),
    path('auth/user/', auth.AuthenticatedUserView.as_view(), name='authUser')
]
