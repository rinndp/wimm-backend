from rest_framework import serializers
from debtors.models import Debtor
from users.models import CustomUser


class CreateDebtorSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = Debtor
        fields = ('name', 'user', 'debt')

    def validate(self, data):
        name = data.get('name')
        user = data.get('user')

        if name is None:
            raise serializers.ValidationError('Name is required')

        if len(name) <= 1:
            raise serializers.ValidationError('Name must have at least 2 characters')

        if not user:
            raise serializers.ValidationError('User is required')

        return data
