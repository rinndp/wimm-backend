from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from creditors.models import Creditor
from credits.serializers import CreateCreditSerializer

class CreateCreditView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data

        serializer = CreateCreditSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            creditor = Creditor.objects.get(id=data.get('creditor'))
            creditor.update_credit()
            return Response({"message":"Credit created correctly"}, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

