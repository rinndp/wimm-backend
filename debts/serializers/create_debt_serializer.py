from rest_framework import serializers

from debts.models.debt_model import Debt


class CreateDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('description', 'debt', 'debtor')

    def validate(self, data):
        description = data.get('description')
        debt = data.get('debt')
        debtor = data.get('debtor')

        if description is None or debtor is None:
            raise serializers.ValidationError('Require fields are missing ("description", "debt", "debtor")')

        if debt == 0:
            raise serializers.ValidationError('Debt cannot be 0')

        return data