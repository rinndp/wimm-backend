from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from creditors.models import Creditor
from creditors.serializers import GetCreditorsByUserSerializer
from users.models import CustomUser


class GetCreditorsByUserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, user_slug):
        if not CustomUser.objects.filter(slug=user_slug).exists():
            return Response({
                "error": "User not found with slug: " + user_slug},
                status=HTTP_404_NOT_FOUND)

        creditors = Creditor.objects.filter(user__slug=user_slug).order_by('-updated_at')
        serializer = GetCreditorsByUserSerializer(creditors, many=True)
        return Response(serializer.data, HTTP_200_OK)
