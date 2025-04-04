from django.views.generic import CreateView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from debtors.serializer.create_debtor_serializer import CreateDebtorSerializer
from users.models import CustomUser


class CreateDebtorView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        debt = data.get("debt")

        if debt is None:
            data["debt"] = 0

        serializer = CreateDebtorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Debtor created correctly"}, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)





