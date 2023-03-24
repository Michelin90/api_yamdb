from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from api_yamdb.api.permissions import IsBossOrReadOnlyPermission
from api_yamdb.api.serializers import ReviewSerializer
from api_yamdb.reviews.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsBossOrReadOnlyPermission,)

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
