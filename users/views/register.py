from django.views import View
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from users.models import CustomUser


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide email and password'}, status=HTTP_400_BAD_REQUEST)

        try:
            CustomUser.objects.create_user(email, password)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)

        return Response({"message": "User created successfully"}, status=HTTP_200_OK)


