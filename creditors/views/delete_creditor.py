from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from creditors.models import Creditor


class DeleteCreditorView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, creditor_id):
        try:
            creditor = Creditor.objects.get(id=creditor_id)
        except Creditor.DoesNotExist:
            return Response(
                {"error":"Creditor not found with id: "+creditor_id},
                status=HTTP_400_BAD_REQUEST)

        creditor.delete()
        return Response({"message":"Creditor deleted correctly"}, HTTP_200_OK)
