from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet

from .permissions import IsBossOrReadOnlyPermission
from .serializers import CommentSerializer
from reviews.models import Review

class CommentViewSet(ModelViewSet):
    permission_classes = [
        IsBossOrReadOnlyPermission,
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)