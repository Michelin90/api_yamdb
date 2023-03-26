from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TitleViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]