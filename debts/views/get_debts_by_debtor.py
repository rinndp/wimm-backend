from django.views import View
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from debtors.models import Debtor
from debts.models import Debt
from debts.serializers.get_debts_by_debtor_serializer import GetDebtsByDebtorSerializer


class GetDebtsByDebtorView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, debtor_id):
        try:
            debtor = Debtor.objects.get(id=debtor_id)
        except Debtor.DoesNotExist:
            return Response({"error":"Debtor not found with id: "+debtor_id}, status=HTTP_400_BAD_REQUEST)

        debts = Debt.objects.filter(debtor=debtor).all()
        serializer = GetDebtsByDebtorSerializer(debts, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
