from django.views import View
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers.register_user_serializer import RegisterUserSerializer


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if CustomUser.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=HTTP_400_BAD_REQUEST)

        serializer = RegisterUserSerializer(data=data)
        if serializer.is_valid():
            CustomUser.objects.create_user(email, password)
            return Response({"message": "User created successfully"}, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)





