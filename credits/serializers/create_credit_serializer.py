from rest_framework import serializers

from credits.models import Credit


class CreateCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = ('description', 'credit', 'creditor',)

        def validate (self, data):
            description = data.get('description')
            creditor = data.get('creditor')
            credit = data.get('credit')

            if description is None or creditor is None:
                raise serializers.ValidationError('Require fields are missing ("description", "credit", "creditor")')

            if credit == 0:
                raise serializers.ValidationError('Credit cannot be 0')

            return data

