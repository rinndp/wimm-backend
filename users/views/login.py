from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if email is None or password is None:
            return Response({"error": 'Email and password are required'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return Response({"message" : 'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({"error": 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        except CustomUser.DoesNotExist:
            return Response({"error": 'Email not found'},status=status.HTTP_400_BAD_REQUEST)

