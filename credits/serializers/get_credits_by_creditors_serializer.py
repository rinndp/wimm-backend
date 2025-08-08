from rest_framework import serializers

from credits.models import Credit


class GetCreditsByCreditorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = ('id', 'description', 'credit', 'updated_at',)