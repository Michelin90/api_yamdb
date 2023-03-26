from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CommentViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
    
urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]