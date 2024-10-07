from rest_framework import viewsets
from .models import Parent, Child
from .serializers import ParentSerializer, childSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = childSerializer

