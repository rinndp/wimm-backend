from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from credits.models import Credit


class DeleteCreditView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, credit_id):
        try:
            credit = Credit.objects.get(id=credit_id)
        except Credit.DoesNotExist:
            return Response({
                "error":"Credit not found with id: "+credit_id},
                 status=HTTP_400_BAD_REQUEST)

        credit.delete()
        credit.creditor.update_credit()
        return Response({"message":"Credit deleted correctly"}, HTTP_200_OK)

