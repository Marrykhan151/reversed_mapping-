from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentViewSet, ChildViewSet

router = DefaultRouter()
router.register(r'parent', ParentViewSet)
router.register(r'children', ChildViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]
