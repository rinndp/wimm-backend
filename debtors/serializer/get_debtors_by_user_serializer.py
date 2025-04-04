from rest_framework import serializers

from debtors.models import Debtor


class GetDebtorsByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtor
        fields = ('id', 'name', 'debt',)



