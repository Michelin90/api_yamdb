from rest_framework import serializers
from reviews.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'bio', 'role'
        ]

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError('Недопустимое имя!')
        return data
