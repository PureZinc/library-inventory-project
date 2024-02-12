from rest_framework import serializers as ser
from .models import Book, UserMembership, BookTracker
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# For authentication
class UserSer(ser.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        UserMembership.objects.create(user=user)
        return user


class LoginSer(ser.Serializer):
    username = ser.CharField()
    password = ser.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username and password:
            raise ser.ValidationError("Both username and password are required")
        
        user = authenticate(username=username, password=password)

        if not user:
            raise ser.ValidationError("Invalid credentials")

        data['user'] = user
        return data


# For everything else
class UserMembershipSer(ser.ModelSerializer):
    class Meta:
        model = UserMembership
        fields = ['id', 'user', 'is_librarian', 'is_member', 'total_books_rented']
        

class BookSer(ser.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year', 'description', 'ISBN', 'stock']
    
    def update(self, instance, validated_data):
        instance.stock = validated_data.get('stock', instance.stock)
        return instance


class BookTrackerSer(ser.ModelSerializer):
    class Meta:
        model = BookTracker
        fields = ['id', 'user', 'book', 'date_rented', 'due_date']
    
    def create(self, validated_data):
        user = self.context['request'].user
        tracker = BookTracker.objects.create(user=user, **validated_data)
        return tracker
    