from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta


def default_due_date():
    return timezone.now() + relativedelta(months=1)


class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_librarian = models.BooleanField(default=False)
    is_member = models.BooleanField(default=True)

    total_books_rented = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    description = models.TextField(blank=True)
    ISBN = models.CharField(max_length=13, unique=True)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title}: by {self.author}"
    

class BookTracker(models.Model):
    user = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    date_rented = models.DateTimeField(default=timezone.now())
    due_date = models.DateField(default=default_due_date)

    def __str__(self):
        return f"{self.user}, {self.book} | due: {self.due_date}"
