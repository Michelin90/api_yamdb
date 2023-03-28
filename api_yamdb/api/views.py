from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from reviews.models import Category, Genre, Title
from serializers import CategorySerializer, GenreSerializer, TitleSerializer
from permissions import AdminOrReadOnlyPermission


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('^name', )


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('category', 'genre', 'name', 'year')
    permissions = AdminOrReadOnlyPermission
