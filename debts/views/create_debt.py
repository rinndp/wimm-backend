from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from debtors.models import Debtor
from debts.models import Debt
from debts.serializers.create_debt_serializer import CreateDebtSerializer


class CreateDebtView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data

        serializer = CreateDebtSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            debtor = Debtor.objects.get(id=data.get('debtor'))
            debtor.update_debt()
            return Response({"message":"Debt created correctly"}, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
