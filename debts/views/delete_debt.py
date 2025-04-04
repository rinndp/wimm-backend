from django.views import View
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from debts.models import Debt


class DeleteDebtView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, debt_id):
        if not debt_id:
            return Response({
                    "error":"/debts/{debt_id} debt_id cannot be null"},
                    status=HTTP_400_BAD_REQUEST)

        try:
            debt = Debt.objects.get(id=debt_id)
        except Debt.DoesNotExist:
            return Response({
                "error":"Debt not found with id: "+debt_id},
                status=HTTP_400_BAD_REQUEST)

        debt.delete()
        Debt.update_debt(debt)
        return Response({"message":"Debt deleted correclty"}, status=HTTP_200_OK)


