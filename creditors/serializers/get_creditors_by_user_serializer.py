from rest_framework import serializers

from creditors.models import Creditor


class GetCreditorsByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creditor
        fields = ('id', 'name', 'credit',)