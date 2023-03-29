from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Title, Review
from user.models import User


class UserValidateSerializer(serializers.ModelSerializer):

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Недопустимое имя!')
        return value


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    review = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True,
        source='title.id'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    description = serializers.CharField(required=False)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class UserSerializer(UserValidateSerializer):

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'bio', 'role', 'email'
        ]


class SignupSerializer(UserValidateSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'confirmation_code']


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (request.method == 'POST'
           and title.reviews.filter(author=author).exists()):
            raise ValidationError('Можно оставить только один отзыв!')
        return data

    def validate_score(self, value):
        if not 1 <= value <= 10:
            raise serializers.ValidationError(
                'Допускается оценка только от 1 до 10!')
        return value

    class Meta:
        fields = '__all__'
        model = Review


class MeSerializer(UserValidateSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'bio', 'email', 'role',
        ]
