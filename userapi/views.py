from django.shortcuts import render
from rest_framework import viewsets , generics
from rest_framework.permissions import AllowAny
from studyuganda.permissions import IsLoggedInUserOrAdmin, IsAdminUser


from userapi.models import User
from userapi.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
          permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
          permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
          permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user