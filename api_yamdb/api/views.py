from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import CommentSerializer, UserSerializer, SignupSerializer
from .permissions import IsBossOrReadOnlyPermission
from .utils import code_generation
from reviews.models import Review, User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = (IsAdminUser,)

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=(IsAuthenticated,),
    )
    def me(self, request):
        if request.method == 'PATCH':
            serializer = UserSerializer(
                request.user,
                data=request.data,
                partial=True,
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class SignupView(views.APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(
                User, username=request.data.get('username')
            )
            confirmation_code = code_generation()
            user.confirmation_code = confirmation_code
            user.save()
            send_mail(
                subject='Код подтверждения',
                message=confirmation_code,
                recipient_list=[user.email],
                from_email=settings.EMAIL_HOST_USER,
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
