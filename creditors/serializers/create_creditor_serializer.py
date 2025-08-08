from rest_framework import serializers
from creditors.models import Creditor
from users.models import CustomUser


class CreateCreditorSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = Creditor
        fields = ('name', 'user',)

    def validate(self, data):
        name = data.get('name')
        user = data.get('user')

        if name is None:
            raise serializers.ValidationError('Name is required')

        if len(name) < 1:
            raise serializers.ValidationError('Name must have at least 2 characters')

        if user is None:
            raise serializers.ValidationError('User is required')

        return data
