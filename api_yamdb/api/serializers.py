from rest_framework import serializers
from reviews.models import User, Comment, Category


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'bio', 'role', 'email'
        ]

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError('Недопустимое имя!')
        return data


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError('Недопустимое имя!')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    review = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')
