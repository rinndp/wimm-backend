from django.views import View
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from debtors.models import Debtor


class DeleteDebtorView(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, debtor_id):
        try:
            debtor = Debtor.objects.get(id=debtor_id)
        except Debtor.DoesNotExist:
            return Response({"error":"Debtor not found with id: "+debtor_id},status=HTTP_400_BAD_REQUEST)

        debtor.delete()
        return Response({"message":"Debtor deleted correctly"}, status=HTTP_200_OK)

