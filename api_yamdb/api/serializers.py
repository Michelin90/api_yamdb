from rest_framework import serializers

from reviews.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    review = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment
