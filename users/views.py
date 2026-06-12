from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.db import IntegrityError
from .models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


class UserListCreate(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):

        search = request.GET.get("search")

        users = User.objects.all()

        # Search functionality
        if search:
            users = users.filter(name__icontains=search)

        # Pagination
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)

        paginator = Paginator(users, limit)

        users_page = paginator.get_page(page)

        serializer = UserSerializer(users_page, many=True)

        return Response({
            "success": True,
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": int(page),
            "data": serializer.data
        })
    def post(self, request):
        
        permission_classes = [IsAuthenticated]
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            try:
                serializer.save()

                return Response({
                    "success": True,
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)

            except IntegrityError:

                return Response({
                    "success": False,
                    "error": "Duplicate email"
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
class UserDetail(APIView):

    def get(self, request, id):

        try:

            user = User.objects.get(id=id)

            serializer = UserSerializer(user)

            return Response({
                "success": True,
                "data": serializer.data
            })

        except User.DoesNotExist:

            return Response({
                "success": False,
                "error": "User not found"
            }, status=404)