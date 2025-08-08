from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from creditors.models import Creditor
from credits.models import Credit
from credits.serializers import GetCreditsByCreditorsSerializer


class GetCreditsByCreditorView(APIView):
    permission_classes = (AllowAny,)

    def get(self,request,creditor_id):
        try:
            creditor = Creditor.objects.get(id=creditor_id)
        except Creditor.DoesNotExist:
            return Response({
                "error":"Creditor not found with id: " +creditor_id},
                 status=status.HTTP_400_BAD_REQUEST)

        credits_by_creditor = Credit.objects.filter(creditor=creditor).order_by('-updated_at')
        serializer = GetCreditsByCreditorsSerializer(credits_by_creditor, many=True)
        return Response(serializer.data, HTTP_200_OK)

