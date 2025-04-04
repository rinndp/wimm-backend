from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from debtors.models import Debtor
from debtors.serializer.get_debtors_by_user_serializer import GetDebtorsByUserSerializer
from users.models import CustomUser


class GetDebtorsByUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, user_slug):
        if not CustomUser.objects.filter(slug=user_slug).exists():
            return Response({
                "error" : "User not found with slug: "+user_slug},
                status=HTTP_404_NOT_FOUND)

        debtors = Debtor.objects.filter(user__slug=user_slug).all()
        serializer = GetDebtorsByUserSerializer(debtors, many=True)
        return Response(serializer.data, status=HTTP_200_OK)