from rest_framework import serializers
from .models import Parent, Child

class childSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child 
        fields = "__all__"

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ["id","children"]
