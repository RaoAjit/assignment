from django.urls import path
from users.views import UserListCreate, UserDetail

urlpatterns = [
    path('users/', UserListCreate.as_view()),
    path('users/<int:id>/', UserDetail.as_view()),
]