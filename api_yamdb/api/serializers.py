from rest_framework import serializers

from api_yamdb.reviews.models import Comment, Category


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
