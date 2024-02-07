from django.contrib import admin
from .models import UserMembership, Book, BookTracker

# Register your models here.
admin.site.register(UserMembership)
admin.site.register(Book)
admin.site.register(BookTracker)
