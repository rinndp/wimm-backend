from rest_framework import serializers

from debts.models import Debt


class GetDebtsByDebtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id', 'description', 'debt')

